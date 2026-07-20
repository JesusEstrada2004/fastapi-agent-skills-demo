from fastapi import APIRouter
from app.models.schemas import (
    PromptRequest,
    PromptAnalysisResponse,
    ControlledResponse
)
from app.services.text_processor import analyze_prompt, generate_controlled_response
from app.services.skill_loader import load_skill_content, get_skill_name

router = APIRouter()


@router.get("/skill")
def get_active_skill():
    """
    Retorna la skill cargada por la API.
    """
    return {
        "skill_name": get_skill_name(),
        "skill_content": load_skill_content()
    }


@router.post("/analyze", response_model=PromptAnalysisResponse)
def analyze_text(request: PromptRequest):
    """
    Analiza un prompt y retorna métricas básicas, nivel de riesgo y recomendación.
    """
    analysis = analyze_prompt(request.prompt)

    return PromptAnalysisResponse(
        original_prompt=request.prompt,
        character_count=len(request.prompt.strip()),
        word_count=len(request.prompt.strip().split()),
        risk_level=analysis["risk_level"],
        is_valid=analysis["is_valid"],
        recommendation=analysis["recommendation"]
    )


@router.post("/generate", response_model=ControlledResponse)
def generate_response(request: PromptRequest):
    """
    Genera una respuesta controlada aplicando las reglas de la skill prompt_guard.
    """
    result = generate_controlled_response(request.prompt)

    return ControlledResponse(
        prompt=request.prompt,
        response=result["response"],
        skill_applied=get_skill_name(),
        behavior=result["behavior"]
    )