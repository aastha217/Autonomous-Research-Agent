from app.rag.retriever import retrieve_relevant_chunks

query = "What are AI agents?"

chunks = retrieve_relevant_chunks(query)

print("\nRetrieved Chunks:\n")

for i, chunk in enumerate(chunks, start=1):
    print(f"\n------ Chunk {i} ------\n")
    print(chunk)