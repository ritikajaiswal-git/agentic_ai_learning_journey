import os
import faiss
import numpy as np
import pickle
from typing import List, Any
from sentence_transformers import SentenceTransformer
from src.learning_rag.embedding import EmbeddingPipeline


# ============================================================
# FAISS VECTOR STORE
# FAISS ek library hai jo numerical embeddings ko store karti
# hai aur unke beech similarity search perform karti hai.
#
# RAG mein iska use:
# Documents -> Chunks -> Embeddings -> FAISS Index -> Search
#
# FAISS original text directly understand nahi karta.
# Ye numerical vectors ke basis par similar content find karta hai.
# ============================================================

class FaissVectorStore:

    # STEP 1: FAISS Vector Store initialize karna
    def __init__(
        self,
        persist_dir: str = "faiss_store",#ye default value h agr object bnate wqt value ni doge to ye value use  hogi
        embedding_model: str = "all-MiniLM-L6-v2",
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):
           #ye avi constructor k part hi chlra,right side local variable h, ar left side self. kre k wo instance variablbn 
        #bn gya h, object k sath in varible ko  use kr kste h
        self.persist_dir = persist_dir

        # FAISS index aur metadata ko permanently save karne ke liye folder
        os.makedirs(self.persist_dir, exist_ok=True)

        self.index = None
        # FAISS index initially empty rahega; isi mein vectors store honge

        self.metadata = []
        # Har vector ke corresponding original text aur details store hongi

        self.embedding_model = embedding_model
        self.model = SentenceTransformer(embedding_model)
        # Pre-trained model load karna jo text ko numerical vectors mein convert karta hai

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        print(f"[INFO] Loaded embedding model: {embedding_model}")


    # STEP 2: Documents se complete FAISS Vector Store build karna
    def build_from_documents(self, documents: List[Any]):

        print(f"[INFO] Building vector store from {len(documents)} documents...")

        # Existing EmbeddingPipeline ko use karke chunking aur embedding karna
        emb_pipe = EmbeddingPipeline(
            model_name=self.embedding_model,
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

        # Bade documents ko smaller chunks mein divide karna
        chunks = emb_pipe.chunk_documents(documents)

        # Har chunk ko numerical vector (embedding) mein convert karna
        embeddings = emb_pipe.embed_chunks(chunks)

        # Har embedding ke saath uska original text map karna
        # Taaki search ke baad original content retrieve kar sakein
        metadatas = [
            {"text": chunk.page_content}
            for chunk in chunks
        ]

        # Embeddings ko FAISS ke required float32 format mein convert karke store karna
        #class k andr wale func ko class k andr call self. s krte h, bhr m object bna k obj, s krte h
        self.add_embeddings(
            np.array(embeddings).astype("float32"),
            metadatas
        )

        # Built FAISS index aur metadata ko local directory mein save karna
        self.save()

        print(f"[INFO] Vector store built and saved to {self.persist_dir}")


    # STEP 3: Embeddings ko FAISS index mein add karna
    #Socho FAISS index ek database jaisa storage structure hai, jisme numerical vectors rakhe jaate hain.
    def add_embeddings(
        self,
        embeddings: np.ndarray,
        metadatas: List[Any] = None
    ):

        # Har embedding vector ki dimensions nikalna
        # Example: all-MiniLM-L6-v2 ke liye dimensions = 384
        dim = embeddings.shape[1]

        # Agar index abhi tak create nahi hua hai toh L2 index banana
        if self.index is None:

            # IndexFlatL2 exact Euclidean distance search karta hai
            # Lower distance ka matlab vectors ek doosre ke closer hain
            self.index = faiss.IndexFlatL2(dim)

        # Saare numerical vectors ko FAISS index mein insert karna
        self.index.add(embeddings)

        # Original text ko vectors ke corresponding order mein store karna
        if metadatas:
            self.metadata.extend(metadatas)


    # STEP 4: FAISS index aur metadata ko local storage mein save karna
    def save(self):

        # FAISS index aur metadata ki file locations prepare karna
        faiss_path = os.path.join(self.persist_dir, "faiss.index")
        meta_path = os.path.join(self.persist_dir, "metadata.pkl")

        # FAISS index ko disk par save karna
        faiss.write_index(self.index, faiss_path)

        # Pickle Python metadata ko binary file mein save karta hai
        with open(meta_path, "wb") as f:
            pickle.dump(self.metadata, f)

        print(f"[INFO] FAISS index and metadata saved to {self.persist_dir}")


    # STEP 5: Previously saved FAISS index aur metadata load karna
    def load(self):

        faiss_path = os.path.join(self.persist_dir, "faiss.index")
        meta_path = os.path.join(self.persist_dir, "metadata.pkl")

        # Disk se previously stored FAISS index load karna
        self.index = faiss.read_index(faiss_path)

        # Pickle file se original text aur metadata retrieve karna
        with open(meta_path, "rb") as f:
            self.metadata = pickle.load(f)

        print(f"[INFO] FAISS index and metadata loaded from {self.persist_dir}")


    # STEP 6: User query ke embedding se similar documents search karna
    def search(self, query: str, top_k: int = 5):

        # STEP 1: User ki query ko numerical vector mein convert karna
            # FAISS text nahi, embeddings par similarity search karta hai
        #model.encode sentence trnasformer clas ka andr k method h
        #split_document recusivetextcharsplittter k andr ata h
            query_embedding = self.model.encode([query])
        
            # STEP 2: FAISS ke required float32 format mein convert karna
            query_embedding = np.array(query_embedding).astype("float32")
        
            # STEP 3: Query vector ke basis par top-k similar vectors find karna
            D, I = self.index.search(query_embedding, top_k)
        
            results = []
        
            # STEP 4: Retrieved vector ke index aur distance ko read karna
        #idx means kon s vector m mila h, mtlb bht sara faiss index h n jo vectors ko store krte, dist mtlb query ar search kitne similar h, 
        #indexflatl2 use hua h mtlb dist jitne km utne similar 
            for idx, dist in zip(I[0], D[0]):
        
                # Invalid index ko skip karna
                if idx == -1:
                    continue
        
                # Retrieved index ka corresponding metadata nikalna
                #idx faiss ar metadata ki same hoti h
                meta = self.metadata[idx]
        
                # Search result mein index, distance aur original text store karna
                results.append({
                    "index": int(idx),
                    "distance": float(dist),
                    "metadata": meta
                })
        
            # STEP 5: Saare relevant search results return karna
            return results

#     Complete flow
# 1. __init__() – FAISS database initialize karna aur settings configure karna.
# 2. build_from_documents() – Documents lena, chunks banana aur unki embeddings generate karna.
# 3. add_embeddings() – Generated numerical vectors ko FAISS index mein store karna.
# 4. save() – FAISS index aur original text ka metadata local directory mein permanently save karna.
# 5. load() – Saved index aur metadata ko dobara load karna.
# 6. search() – User query ki embedding ke basis par top-k similar vectors find karna aur unka original text return karna.
