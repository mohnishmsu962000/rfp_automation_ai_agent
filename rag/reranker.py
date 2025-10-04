import cohere
import os
from dotenv import load_dotenv

load_dotenv()

cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))


def rerank(query: str, chunks: list, top_k: int = 5) -> list:
    
    results = cohere_client.rerank(
        query=query, 
        documents=[chunk['chunk_content'] for chunk in chunks], 
        top_n=top_k,
        model="rerank-english-v3.0"
        )
    
    reranked_chunks = [chunks[result.index] for result in results.results]

    return reranked_chunks
