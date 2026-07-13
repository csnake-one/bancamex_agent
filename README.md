# bancamex_agent
Proyecto que pretende crear un agente que pueda responder las preguntas de los usuarios de la fintech BancaMex. Challenge para entregar en G10 de aluralatam

# Agente de Consultas - Banca Mex

Este repositorio contiene el agente inteligente basado en arquitecturas RAG utilizando LangGraph y Gemini para responder consultas estrictamente limitadas a las políticas internas de Banca Mex.

## Estructura
El proyecto sigue un diseño modular dividiendo la base de datos de vectores (`ChromaDB`), la orquestación del agente (`LangGraph`) y las interfaces de ejecución.

## Ejecución rápida
1. Configure su entorno e instale las dependencias.
2. Inserte su `GOOGLE_API_KEY` en el archivo `.env`.
3. Ejecute `python main.py` para interactuar con el agente por consola.
