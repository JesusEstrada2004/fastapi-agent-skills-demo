from app.core.config import MAX_PROMPT_LENGTH


RISK_KEYWORDS = [
    "hackear",
    "robar",
    "contraseña",
    "malware",
    "ataque",
    "phishing"
]


def analyze_prompt(prompt: str) -> dict:
    """
    Analiza un prompt y determina si cumple con las reglas básicas definidas.
    """
    cleaned_prompt = prompt.strip()
    character_count = len(cleaned_prompt)
    word_count = len(cleaned_prompt.split())

    if not cleaned_prompt:
        return {
            "risk_level": "high",
            "is_valid": False,
            "recommendation": "El prompt está vacío. Solicita más contexto al usuario."
        }

    if character_count > MAX_PROMPT_LENGTH:
        return {
            "risk_level": "medium",
            "is_valid": False,
            "recommendation": f"El prompt supera el límite permitido de {MAX_PROMPT_LENGTH} caracteres."
        }

    lower_prompt = cleaned_prompt.lower()

    if any(keyword in lower_prompt for keyword in RISK_KEYWORDS):
        return {
            "risk_level": "high",
            "is_valid": False,
            "recommendation": "El prompt contiene términos sensibles. Responder de forma segura."
        }

    return {
        "risk_level": "low",
        "is_valid": True,
        "recommendation": "El prompt es válido y puede procesarse normalmente."
    }


def generate_controlled_response(prompt: str) -> dict:
    """
    Genera una respuesta controlada según el análisis del prompt.
    """
    analysis = analyze_prompt(prompt)

    if not analysis["is_valid"]:
        return {
            "response": (
                "No puedo procesar directamente esta solicitud porque no cumple "
                "con las reglas de validación definidas por la skill. "
                f"Recomendación: {analysis['recommendation']}"
            ),
            "behavior": "restricted"
        }

    return {
        "response": (
            "Solicitud recibida correctamente. El agente puede continuar con el "
            "procesamiento del prompt siguiendo las reglas de la skill prompt_guard."
        ),
        "behavior": "allowed"
    }