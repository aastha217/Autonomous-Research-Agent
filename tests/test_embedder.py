from app.rag.embedder import embed_text

embedding = embed_text(
    "What are AI agents?"
)

print(len(embedding))