import os
from dotenv import load_dotenv
from src.learning_rag.vectorstore import FaissVectorStore
from langchain_groq import ChatGroq

# .env file se API keys aur environment variables load kar rhe hain
load_dotenv()


class RAGSearch:

    # FAISS Vector Store aur Groq LLM initialize kar rhe hain
    def __init__(
        self,
        persist_dir: str = "faiss_store",
        embedding_model: str = "all-MiniLM-L6-v2",
        llm_model: str = "openai/gpt-oss-120b"
    ):

        # FAISS Vector Store ka object create kar rhe hain
        self.vectorstore = FaissVectorStore(
            persist_dir,
            embedding_model
        )

        # Check kar rhe hain ki FAISS index aur metadata files available hain ya nahi
        faiss_path = os.path.join(persist_dir, "faiss.index")
        meta_path = os.path.join(persist_dir, "metadata.pkl")

        # Agar dono files available nahi hain, toh documents se index build karenge
        if not (os.path.exists(faiss_path) and os.path.exists(meta_path)):

            # Data folder se documents load kar rhe hain
            from src.learning_rag.data_loader import load_all_documents
            docs = load_all_documents("data")

            # Documents ki embeddings generate karke FAISS index build aur save kar rhe hain
            self.vectorstore.build_from_documents(docs)

        else:
            # Existing FAISS index aur metadata load kar rhe hain
            self.vectorstore.load()

        # .env file se Groq API key access kar rhe hain
        groq_api_key = os.getenv("GROQ_API_KEY")

        # Groq LLM initialize kar rhe hain
        self.llm = ChatGroq(
            groq_api_key=groq_api_key,
            model_name=llm_model
        )

        print(f"[INFO] Groq LLM initialized: {llm_model}")

    # User query ke relevant documents retrieve karke answer summarize karne ke liye
    def search_and_summarize(self, query: str, top_k: int = 5) -> str:

        # FAISS se query ke basis par top-k relevant documents retrieve kar rhe hain
        results = self.vectorstore.search(query, top_k=top_k)

        # Retrieved documents ke metadata se original text extract kar rhe hain
        texts = [
            r["metadata"].get("text", "")
            for r in results if r["metadata"]
        ]

        # Saare retrieved texts ko ek context mein combine kar rhe hain
        context = "\n\n".join(texts)

        # Agar relevant context nahi mila toh message return karenge
        if not context:
            return "No relevant documents found."

        # Retrieved context aur user query ko LLM ke prompt mein combine kar rhe hain
        prompt = f"""Summarize the following context for the query: '{query}'

Context:
{context}

Answer:"""

        # Groq LLM ko prompt bhejkar response generate kar rhe hain
        response = self.llm.invoke([prompt])

        # Generated summary return kar rhe hain
        return response.content