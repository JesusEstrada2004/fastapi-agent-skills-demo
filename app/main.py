from fastapi import FastAPI
from app.routes.text_routes import router as text_router

app = FastAPI(
    title="FastAPI Agent Skills Demo",
    description="API básica que integra una skill agentica para controlar el procesamiento de prompts.",
    version="1.0.0"
)

app.include_router(text_router, prefix="/api/v1", tags=["Prompt Processing"])


@app.get("/")
def root():
    return {
        "message": "FastAPI Agent Skills Demo is running",
        "docs": "/docs"
    }