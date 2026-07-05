from app.rag.embedder import embed_text
from app.rag.vector_store import search


def retrieve_relevant_chunks(query: str, n_results: int = 5):
    """
    Retrieve the most relevant document chunks
    for a given user query.
    """

    query_embedding = embed_text(query)

    results = search(
        query_embedding=query_embedding,
        n_results=n_results
    )

    return results["documents"][0]