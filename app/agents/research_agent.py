from app.logger import logger

from app.tools.search import search_web
from app.tools.scraper import scrape_article

from app.rag.chunker import chunk_text
from app.rag.embedder import embed_text

from app.rag.vector_store import (
    store_chunks,
    clear_collection
)

from app.rag.retriever import retrieve_relevant_chunks
from app.rag.generator import generate_answer


def research(query: str):

    logger.info("Starting new research session...")

    # Clear old vectors before starting a new search
    clear_collection()

    logger.info(f"Searching for: {query}")

    search_results = search_web(query)

    logger.info(f"Found {len(search_results)} search results.")

    for result in search_results:

        try:
            logger.info(f"Reading article: {result['title']}")

            article = scrape_article(result["url"])

            if not article:
                logger.warning(
                    f"Skipping article (no content): {result['title']}"
                )
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

            logger.info(
                f"Stored {len(chunks)} chunks from '{result['title']}'"
            )

        except Exception as e:

            logger.error(
                f"Failed to process '{result['title']}': {e}"
            )

            continue

    logger.info("Retrieving relevant document chunks...")

    retrieved_data = retrieve_relevant_chunks(query)

    logger.info("Generating research report...")

    answer = generate_answer(
        query,
        retrieved_data
    )

    logger.info("Research report generated successfully.")

    return answer