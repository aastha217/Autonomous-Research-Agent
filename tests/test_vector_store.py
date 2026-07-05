from app.tools.scraper import scrape_article
from app.rag.chunker import chunk_text
from app.rag.embedder import embed_text
from app.rag.vector_store import store_chunks, search

url = "https://www.ibm.com/think/topics/ai-agents"

text = scrape_article(url)

chunks = chunk_text(text)

embeddings = [
    embed_text(chunk)
    for chunk in chunks
]

store_chunks(chunks, embeddings)

query_embedding = embed_text("What are AI agents?")

results = search(query_embedding)

print(results["documents"][0])