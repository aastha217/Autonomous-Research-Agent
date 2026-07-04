from app.tools.scraper import scrape_article
from app.rag.chunker import chunk_text

url = "https://www.ibm.com/think/topics/ai-agents"

text = scrape_article(url)

chunks = chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])