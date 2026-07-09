# Autonomous Research Agent

Autonomous Research Agent is a Retrieval-Augmented Generation (RAG) application that performs end-to-end web research. It searches the web, retrieves and ranks relevant information, and generates structured research reports with source citations using a Large Language Model.

## Overview

The application automates the research workflow by searching the web, extracting relevant content, storing semantic embeddings in a vector database, retrieving the most relevant information, and generating a comprehensive research report grounded in retrieved sources.

## Workflow


```text
User Query
    │
    ▼
Web Search (Tavily API)
    │
    ▼
Web Scraping (BeautifulSoup)
    │
    ▼
Document Chunking (LangChain)
    │
    ▼
Embedding Generation (Sentence Transformers)
    │
    ▼
ChromaDB Vector Store
    │
    ▼
Semantic Retrieval
    │
    ▼
Report Generation (Groq – Llama 3)
    │
    ▼
Markdown Research Report
```


The generated report is grounded in retrieved web content rather than relying solely on the language model's internal knowledge, improving factual relevance and reducing unsupported information.

## Features

- Automated web search using Tavily
- Web scraping with BeautifulSoup
- Recursive document chunking
- Semantic embeddings using Sentence Transformers
- Persistent vector storage with ChromaDB
- AI-powered report generation using Groq (Llama 3)
- FastAPI REST API
- Automatic Markdown report generation

## Tech Stack

| Layer                | Technology                  |
|----------------------|-----------------------------|
| Backend              | FastAPI                     |
| Programming Language | Python 3.13                 |
| Search Engine        | Tavily API                  |
| Web Scraping         | BeautifulSoup               |
| Text Processing      | LangChain Text Splitters    |
| Embedding Model      | Sentence Transformers       |
| Vector Store         | ChromaDB                    |
| LLM                  | Groq (Llama 3.3)            |

## Installation

Clone the repository:

```bash
git clone https://github.com/aastha217/Autonomous-Research-Agent.git
cd Autonomous-Research-Agent
```

Create and activate a virtual environment:

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## API

### POST `/research`

Request:

```json
{
  "query": "What are AI agents?"
}
```

Response:

```json
{
  "query": "What are AI agents?",
  "report": "...",
  "saved_to": "reports/report_YYYYMMDD_HHMMSS.md"
}
```

## Project Structure

```text
Autonomous-Research-Agent/
│
├── app/
│   ├── agents/
│   ├── rag/
│   ├── tools/
│   ├── logger.py
│   └── main.py
│
├── tests/
├── reports/
├── logs/
├── requirements.txt
├── README.md
└── .gitignore
```

## Future Improvements

- PDF report export
- Frontend dashboard
- Docker support
- Cloud deployment
- Multi-agent research workflow

## Author

**Aastha**


B.Tech in Computer Science and Engineering  
Malaviya National Institute of Technology (MNIT), Jaipur