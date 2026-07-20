# FastAPI Agent Skills Demo

## Descripción general

Este proyecto consiste en una API básica desarrollada con FastAPI que permite analizar prompts enviados por un usuario y generar respuestas controladas. La API integra una skill agentica personalizada llamada `prompt-guard`, ubicada en el directorio `.github/skills/prompt-guard/`.

El objetivo principal del proyecto es demostrar cómo una API puede organizarse de forma modular y cómo una skill puede influir en el comportamiento de un agente de IA al momento de procesar solicitudes.

---

## Objetivo del proyecto

El objetivo de esta actividad es diseñar e implementar una API básica utilizando FastAPI, integrando una skill personalizada bajo el estándar Agent Skills.

La actividad permite demostrar:

- Diseño de una API con FastAPI.
- Separación de responsabilidades entre rutas, servicios, modelos y configuración.
- Implementación de endpoints funcionales.
- Creación de una skill personalizada mediante un archivo `SKILL.md`.
- Integración de la skill para controlar o modificar el comportamiento del agente.
- Uso consciente de herramientas de IA durante el desarrollo.

---

## Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- Pydantic
- GitHub
- Visual Studio Code
- Agent Skills mediante archivo `SKILL.md`

---

## Estructura del proyecto

```text
fastapi-agent-skills-demo/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── routes/
│   │   └── text_routes.py
│   │
│   └── services/
│       ├── text_processor.py
│       └── skill_loader.py
│
├── .github/
│   └── skills/
│       └── prompt-guard/
│           └── SKILL.md
│
├── requirements.txt
└── README.md

