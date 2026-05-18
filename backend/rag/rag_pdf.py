from pypdf import PdfReader
import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()
collection = client.get_or_create_collection("pdf_docs")

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def ingest_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

    chunks = full_text.split(". ")

    for i, chunk in enumerate(chunks):
        embedding = embed_model.encode(chunk).tolist()

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[str(i)]
        )

def search_pdf(query):
    embedding = embed_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    return results["documents"][0]