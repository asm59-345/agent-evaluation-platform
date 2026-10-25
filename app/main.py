
from fastapi import FastAPI
from app.api.agents import router as agents_router

app = FastAPI(
    title="AI Agent Evaluation Platform",
    description="Evaluate AI agents for accuracy, reliability, safety, latency, and cost.",
    version="1.0.0",
)

# Register Agents API
app.include_router(agents_router)


@app.get("/")
def home():
    return {
        "message": "AI Agent Evaluation Platform is running!",
        "status": "success",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
