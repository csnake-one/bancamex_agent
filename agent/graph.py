#llamadas a Gemini y logica de LangChain

from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from agent.database import inicializar_o_cargar_db
from agent.prompts import PROMPT_AGENTE
import os

# Definición del Estado del Grafo
class AgenteState(TypedDict):
    pregunta: str
    contexto: str
    respuesta: str

# Inicialización de recursos globales para el agente
retriever = inicializar_o_cargar_db()
llm = ChatGoogleGenerativeAI(model="models/gemini-3.6-flash", temperature=0.0)

def nodo_recuperar_informacion(state: AgenteState) -> dict:
    """Nodo encargado de consultar ChromaDB usando la pregunta del usuario."""
    pregunta = state["pregunta"]
    documentos = retriever.invoke(pregunta)
    # Unimos los fragmentos recuperados en un solo string de contexto
    contexto_unido = "\n\n".join([doc.page_content for doc in documentos])
    return {"contexto": contexto_unido}

def nodo_generar_respuesta(state: AgenteState) -> dict:
    """Nodo encargado de enviar el prompt estructurado a Gemini."""
    prompt_formateado = PROMPT_AGENTE.format(
        contexto=state["contexto"],
        pregunta=state["pregunta"]
    )
    respuesta_modelo = llm.invoke(prompt_formateado)
    return {"respuesta": respuesta_modelo.content}

def construir_grafo():
    """Orquesta el flujo utilizando LangGraph."""
    workflow = StateGraph(AgenteState)

    # Definir los nodos de procesamiento
    workflow.add_node("recuperador", nodo_recuperar_informacion)
    workflow.add_node("generador", nodo_generar_respuesta)

    # Definir el flujo lineal controlado
    workflow.set_entry_point("recuperador")
    workflow.add_edge("recuperador", "generador")
    workflow.add_edge("generador", END)

    return workflow.compile()
