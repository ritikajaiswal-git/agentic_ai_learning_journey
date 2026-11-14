# # data_loader.py se load_all_documents function import kar rhe hain
# from src.learning_rag.data_loader import load_all_documents

# # Example usage
# if __name__ == "__main__":

#     # Data folder se saare documents load kar rhe hain
#     docs = load_all_documents("data")

#     # Loaded documents ko display kar rhe hain
#     print(docs)

#     #terminal m write app.py to check working or not(sb document format m h content ar sb hcij ab)

#     # avi hmlg wo embedding.py ko check kr rhe h
#     # Document loading aur embedding pipeline ke functions/classes import kar rhe hain
# from src.learning_rag.data_loader import load_all_documents
# from src.learning_rag.embedding import EmbeddingPipeline


# # Main program yahin se execute hoga
# if __name__ == "__main__":

#     # STEP 1: Data folder se saare supported documents load kar rhe hain
#     docs = load_all_documents("data")

#     # STEP 2: Documents ko chhote chunks mein divide kar rhe hain
#     pipeline = EmbeddingPipeline()
#     chunks = pipeline.chunk_documents(docs)

#     # STEP 3: Har chunk ko numerical vector (embedding) mein convert kar rhe hain
#     chunk_vectors = pipeline.embed_chunks(chunks)

#     # STEP 4: Generated embeddings print kar rhe hain
#     print(chunk_vectors)


#     #checking vectorwala

# from src.learning_rag.data_loader import load_all_documents
# from src.learning_rag.vectorstore import FaissVectorStore

# # Main program yahin se execute hoga
# if __name__ == "__main__":

#     # STEP 1: Data folder se documents load kar rhe hain
#     docs = load_all_documents("data")

#     # STEP 2: FAISS Vector Store initialize kar rhe hain
#     store = FaissVectorStore("faiss_store")

#     # STEP 3: Documents ko chunks mein split karke embeddings generate,
#     # FAISS index build aur disk par save kar rhe hain
#     store.build_from_documents(docs)

#     # STEP 4: Query ke basis par top 3 similar documents search kar rhe hain
#     print(store.search("What is RAG? Explain its workflow.", top_k=3))
from src.learning_rag.search import RAGSearch

# Main program yahin se execute hoga
if __name__ == "__main__":

    # STEP 1: Complete RAG Search pipeline initialize kar rhe hain
    # Iske andar FAISS index load/build aur Groq LLM initialize hoga
    rag_search = RAGSearch()

    # STEP 2: User ki query define kar rhe hain
    query = "What is rag nd its pipeline?"

    # STEP 3: Query ke liye top 3 relevant documents retrieve
    # aur Groq LLM se unka answer summarize karwa rhe hain
    summary = rag_search.search_and_summarize(query, top_k=3)

    # STEP 4: Final generated answer display kar rhe hain
    print("Summary:", summary)