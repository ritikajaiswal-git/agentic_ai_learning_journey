
from pathlib import Path
from typing import List, Any

# PDF, TXT, CSV, Word aur JSON files ko read karne ke loaders
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    Docx2txtLoader,
    JSONLoader
)
from langchain_community.document_loaders.excel import UnstructuredExcelLoader


def load_all_documents(data_dir: str) -> List[Any]:
    """
    Given data directory se files load karke
    unhe LangChain Document objects mein convert karta hai.
    """

    # User ke diye hue folder path ko absolute path mein convert kar rhe hain
    data_path = Path(data_dir).resolve()

    # Saari loaded files ke Document objects collect karne ke liye list
    documents = []

    # 1. PDF FILES

    # Folder aur uske subfolders mein jitni bhi PDF files hain unhe find kar rhe hain
    pdf_files = list(data_path.glob("**/*.pdf"))

    # Total kitni PDF files mili hain, unka count print kar rhe hain
    print(f"[DEBUG] Found {len(pdf_files)} PDF files")

    # Ek-ek PDF file ko read karne ke liye loop chala rhe hain
    for pdf_file in pdf_files:
        try:
            # PDFLoader ko file ka path dekar loader object create kar rhe hain
            loader = PyPDFLoader(str(pdf_file))

            # PDF ke pages ka text extract karke Document objects bana rhe hain
            loaded = loader.load()

            # Loaded documents ko main list mein add kar rhe hain
            documents.extend(loaded)

            # Check kar rhe hain ki current PDF se kitne documents load hue
            print(f"[DEBUG] Loaded {len(loaded)} PDF docs from {pdf_file}")

        except Exception as e:
            # Kisi PDF ko read karte waqt error aaye toh usse print kar rhe hain
            print(f"[ERROR] Failed to load PDF {pdf_file}: {e}")

    # 2. TEXT FILES
    # TODO: TXT files ko load karke documents list mein add karna

    # 3. CSV FILES
    # TODO: CSV files ko load karke documents list mein add karna

    # 4. EXCEL FILES
    # TODO: Excel files ko load karke documents list mein add karna

    # 5. WORD FILES
    # TODO: Word files ko load karke documents list mein add karna

    # 6. JSON FILES
    # TODO: JSON files ko load karke documents list mein add karna

    # Sabhi formats se total kitne documents load hue, count print kar rhe hain
    print(f"Total documents loaded: {len(documents)}")

    # Loaded documents ki complete list return kar rhe hain
    return documents

# in app.py , we will check ye kam kr rha h ya ni,isi function ar code ko waha import krenge ar check krege
