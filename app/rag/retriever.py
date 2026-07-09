from app.rag.embedder import embed_text
from app.rag.vector_store import search


def retrieve_relevant_chunks(query: str, n_results: int = 5):

    query_embedding = embed_text(query)

    results = search(
        query_embedding=query_embedding,
        n_results=n_results
    )

    return {
        "documents": results["documents"][0],
        "metadata": results["metadatas"][0]
    }