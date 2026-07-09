import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)


def generate_answer(question: str, retrieved_data):

    documents = retrieved_data["documents"]
    metadata = retrieved_data["metadata"]

    context = "\n\n".join(documents)

    references = ""

    for i, source in enumerate(metadata, start=1):
        references += (
            f"[{i}] {source['title']}\n"
            f"{source['url']}\n\n"
        )

    prompt = f"""
You are an expert AI research analyst.

Use ONLY the supplied context to answer the user's question.

Context:
{context}

Question:
{question}

Create a professional report with the following structure:

# Research Report

## Executive Summary

## Key Findings

## Detailed Analysis

## Conclusion

## References

Use ONLY these references:

{references}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful research assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content