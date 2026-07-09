import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")


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

Answer ONLY using the provided context.

=========================
CONTEXT
=========================

{context}

=========================
QUESTION
=========================

{question}

Generate a professional research report using this structure:

# Research Report

## Executive Summary

Provide a short summary.

## Key Findings

List the main findings using bullet points.

## Detailed Analysis

Provide a detailed explanation using only the supplied context.

## Conclusion

Summarize the research in a few sentences.

## References

Use ONLY the following references.

{references}
"""

    last_exception = None

    # Retry up to 3 times if Gemini is temporarily busy
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )

            return response.text

        except Exception as e:
            last_exception = e
            print(f"Attempt {attempt + 1}/3 failed.")
            print(e)

            if attempt < 2:
                print("Retrying in 5 seconds...\n")
                time.sleep(5)

    raise last_exception