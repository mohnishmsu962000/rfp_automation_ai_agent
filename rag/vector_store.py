import chromadb
from rag.chunker import chunk_document

chroma_client = chromadb.PersistentClient()


def initialize_collection(company_id):
    collection = chroma_client.get_or_create_collection(f"company_{company_id}")

    return collection


def add_documents_to_collection(
    company_id: str, documents: list, metadatas: list, ids: list
):
    collection = chroma_client.get_collection(f"company_{company_id}")

    collection.add(documents=documents, metadatas=metadatas, ids=ids)


def get_collection(company_id):
    return chroma_client.get_collection(f"company_{company_id}")
