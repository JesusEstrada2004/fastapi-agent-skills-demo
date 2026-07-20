from app.core.config import SKILL_PATH


def load_skill_content() -> str:
    """
    Carga el contenido de la skill personalizada desde .github/skills/.
    """
    if not SKILL_PATH.exists():
        return "No skill found."

    return SKILL_PATH.read_text(encoding="utf-8")


def get_skill_name() -> str:
    """
    Retorna el nombre lógico de la skill utilizada por la API.
    """
    return "prompt_guard"