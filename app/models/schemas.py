from pydantic import BaseModel, Field


class PromptRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=1,
        description="Texto enviado por el usuario para ser analizado o procesado."
    )


class PromptAnalysisResponse(BaseModel):
    original_prompt: str
    character_count: int
    word_count: int
    risk_level: str
    is_valid: bool
    recommendation: str


class ControlledResponse(BaseModel):
    prompt: str
    response: str
    skill_applied: str
    behavior: str