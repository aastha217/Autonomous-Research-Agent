from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pathlib import Path
from datetime import datetime

from app.agents.research_agent import research
from app.logger import logger

app = FastAPI(
    title="Autonomous Research Agent",
    description="""
An AI-powered Autonomous Research Agent built using:

- Tavily Search
- BeautifulSoup Web Scraping
- Sentence Transformers
- ChromaDB
- Retrieval-Augmented Generation (RAG)
- Groq LLM
- FastAPI
""",
    version="1.0.0"
)

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)


class ResearchRequest(BaseModel):
    query: str = Field(
        ...,
        example="What are AI agents?"
    )


@app.get("/")
def home():
    return {
        "status": "running",
        "project": "Autonomous Research Agent",
        "version": "1.0.0"
    }
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Autonomous Research Agent"
    }


@app.post("/research")
def generate_report(request: ResearchRequest):

    try:

        logger.info(f"Received query: {request.query}")

        report = research(request.query)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = REPORTS_DIR / f"report_{timestamp}.md"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(report)

        logger.info(f"Report saved to {filename}")

        return {
            "query": request.query,
            "report": report,
            "saved_to": str(filename)
        }

    except Exception as e:

        logger.error(str(e))

        raise HTTPException(
            status_code=500,
            detail="Failed to generate research report."
        )