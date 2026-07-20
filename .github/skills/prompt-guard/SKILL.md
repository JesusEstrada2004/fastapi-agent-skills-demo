---
name: prompt-guard
description: Skill agentica para validar prompts antes de que el agente interactúe con la API. Controla entradas vacías, textos demasiado largos y solicitudes potencialmente riesgosas.
version: 1.0.0
author: Alejandro Estrada
---

# Prompt Guard Skill

## Propósito

Esta skill define reglas para que un agente de IA procese solicitudes de usuario de forma controlada antes de interactuar con la API desarrollada en FastAPI.

La skill busca evitar que el agente responda de manera automática ante entradas incompletas, ambiguas o potencialmente riesgosas.

## Cuándo usar esta skill

El agente debe usar esta skill cuando:

1. Reciba un prompt enviado por un usuario.
2. Necesite validar si la entrada es clara y suficiente.
3. Deba decidir si puede generar una respuesta normal o si debe restringir la respuesta.
4. Interactúe con los endpoints `/api/v1/analyze` o `/api/v1/generate`.

## Reglas de comportamiento

El agente debe aplicar las siguientes reglas:

1. Si el prompt está vacío, debe solicitar más información al usuario.
2. Si el prompt supera el límite permitido, debe pedir una versión más breve.
3. Si el prompt contiene términos sensibles o riesgosos, debe responder de forma segura.
4. Si el prompt es válido, puede continuar con el procesamiento.
5. El agente no debe asumir información que el usuario no haya proporcionado.
6. El agente debe explicar de forma clara por qué una solicitud fue restringida.

## Integración con la API

Esta skill modifica el comportamiento del agente indicando que debe validar la solicitud antes de generar una respuesta.

Flujo esperado:

1. El usuario envía un prompt.
2. El agente consulta o aplica las reglas de esta skill.
3. La API analiza el prompt mediante el endpoint `/api/v1/analyze`.
4. Si el prompt es válido, el agente puede usar `/api/v1/generate`.
5. Si el prompt no es válido, el agente responde con una advertencia o solicitud de aclaración.

## Responsabilidad técnica

Esta skill no reemplaza la lógica de seguridad de la API. Su función es guiar el comportamiento del agente y complementar la validación implementada en el backend.