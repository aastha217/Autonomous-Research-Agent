from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from datetime import datetime

from app.agents.research_agent import research

app = FastAPI(
    title="Autonomous Research Agent",
    version="1.0.0"
)

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)


class ResearchRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {
        "message": "Autonomous Research Agent API is running!"
    }


@app.post("/research")
def generate_research(request: ResearchRequest):

    report = research(request.query)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = REPORTS_DIR / f"report_{timestamp}.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)

    return {
        "query": request.query,
        "report": report,
        "saved_to": str(filename)
    }