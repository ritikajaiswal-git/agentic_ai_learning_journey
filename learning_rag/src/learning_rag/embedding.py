from typing import List, Any
# Documents ko chunks mein split karne ke liye
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np

# Embedding aur document chunking ka complete pipeline manage karne ke liye class
class EmbeddingPipeline:

    # Model aur chunking settings initialize kar rhe hain
    def __init__(self, model_name: str = "all-MiniLM-L6-v2",
                 chunk_size: int = 1000, chunk_overlap: int = 200):

        self.chunk_size = chunk_size
        # Har chunk mein maximum kitne characters honge

        self.chunk_overlap = chunk_overlap
        # Consecutive chunks mein kitne characters common rahenge

        self.model = SentenceTransformer(model_name)
        # Pre-trained model load kar rhe hain, jo text ko embeddings mein convert karega

        print(f"[INFO] Loaded embedding model: {model_name}")

    # Bade documents ko chhote, manageable chunks mein divide karne ke liye
    def chunk_documents(self, documents: List[Any]) -> List[Any]:

        # Documents ko defined size ke chunks mein split karne ke liye splitter
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            # Chunk ki length characters mein calculate hogi

            separators=["\n\n", "\n", " ", ""]
            # Pehle paragraph, phir line, phir space aur last mein character se split karega
        )

        # Documents ko actual chunks mein convert kar rhe hain
        chunks = splitter.split_documents(documents)

        # Total documents aur generated chunks ka count show kar rhe hain
        print(f"[INFO] Split {len(documents)} documents into {len(chunks)} chunks.")

        # Generated chunks return kar rhe hain
        return chunks
    # Documents ke chunks ko numerical embeddings (vectors) mein convert karne ke liye
    def embed_chunks(self, chunks: List[Any]) -> np.ndarray:

        # Har chunk ka text extract kar rhe hain
            texts = [chunk.page_content for chunk in chunks]
        
            # Kitne chunks ki embeddings generate hongi, show kar rhe hain
            print(f"[INFO] Generating embeddings for {len(texts)} chunks...")
        
            # Pre-trained SentenceTransformer model se text ko vectors mein convert kar rhe hain
            embeddings = self.model.encode(texts, show_progress_bar=True)
        
            # Generated embeddings ka shape (number of chunks, vector dimensions) show karega
            print(f"[INFO] Embeddings shape: {embeddings.shape}")
        
            # Generated numerical vectors return kar rhe hain
            return embeddings
        
#app.py m jake ab ikso test krege ki hua h ya ni 