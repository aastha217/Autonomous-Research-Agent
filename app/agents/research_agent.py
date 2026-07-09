from app.tools.search import search_web
from app.tools.scraper import scrape_article
from app.rag.chunker import chunk_text
from app.rag.embedder import embed_text
from app.rag.vector_store import store_chunks, clear_collection
from app.rag.retriever import retrieve_relevant_chunks
from app.rag.generator import generate_answer


def research(query: str):

    # Start with a fresh collection for this research session
    clear_collection()

    print("Searching the web...")

    search_results = search_web(query)

    for result in search_results:

        print(f"Reading: {result['title']}")

        article = scrape_article(result["url"])

        if not article:
            continue

        chunks = chunk_text(article)

        embeddings = [
            embed_text(chunk)
            for chunk in chunks
        ]

        store_chunks(
            chunks=chunks,
            embeddings=embeddings,
            title=result["title"],
            url=result["url"]
        )

    context = retrieve_relevant_chunks(query)

    answer = generate_answer(
        query,
        context
    )

    return answer