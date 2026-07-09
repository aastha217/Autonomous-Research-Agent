from app.rag.retriever import retrieve_relevant_chunks
from app.rag.generator import generate_answer

question = "What are AI agents?"

chunks = retrieve_relevant_chunks(question)

answer = generate_answer(
    question,
    chunks
)

print(answer)