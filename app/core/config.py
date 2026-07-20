from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SKILL_PATH = BASE_DIR / ".github" / "skills" / "prompt_guard" / "SKILL.md"

MAX_PROMPT_LENGTH = 500