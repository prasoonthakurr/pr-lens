from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(title="Codebase & PR Review Agent")

app.include_router(health_router)