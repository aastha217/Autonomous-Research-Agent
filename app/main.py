from fastapi import FastAPI
from pydantic import BaseModel

from app.agents.research_agent import research

app = FastAPI(
    title="Autonomous Research Agent",
    description="RAG-powered AI research assistant using Tavily, ChromaDB, Sentence Transformers, and Groq.",
    version="1.0.0"
)


class ResearchRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {
        "status": "running",
        "project": "Autonomous Research Agent"
    }


@app.post("/research")
def generate_report(request: ResearchRequest):

    report = research(request.query)

    return {
        "query": request.query,
        "report": report
    }