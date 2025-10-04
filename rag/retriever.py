from rag.vector_store import get_collection
from rag.rerank import rerank_chunks


def retrieve(query: str, company_id: str, top_k=5) -> list:
    collection = get_collection(company_id)
    results = collection.query(query_texts=[query], n_results=top_k * 3)

    chunks = []
    for i in range(len(results["ids"][0])):
        chunk = {
            "chunk_content": results["documents"][0][i],
            "metadatas": results["metadatas"][0][i],
            "chunk_id": results["ids"][0][i],
            "distance": results["distances"][0][i],
        }
        chunks.append(chunk)

    reranked_chunks = rerank_chunks(query, chunks, top_k)

    return reranked_chunks
