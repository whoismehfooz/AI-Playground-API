from fastapi import FastAPI , status
from app.services.ai_services import (generate_response,generate_structured_response)
from app.schemas import (GeneralRequest, GeneralResponse,StructuredAIResponse)
from app.exceptions.handlers import register_exception_handlers
from app.logging_config import configure_logging


app = FastAPI(
    title="AI-Playground-API",
    description="Backend API for experimenting with LLM-powered functionality.",
    version="v1.0.0")

register_exception_handlers(app)
configure_logging()

@app.get('/')
async def root():
    return {"message: AI Playground API is running"}

@app.get('/health')
async def health_check():
    return {
        "status": "healthy",
        "service": "AI-Playground-API",
        "version": app.version
    }

@app.post("/generate",response_model=GeneralResponse,status_code=status.HTTP_200_OK)
async def generate(request:GeneralRequest):
    return generate_response(request)


@app.post("/generate/structured",response_model=StructuredAIResponse,status_code=status.HTTP_200_OK)
async def generate_structured(request:GeneralRequest):
    return generate_structured_response(request)