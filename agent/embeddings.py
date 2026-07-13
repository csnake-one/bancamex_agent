import os
import requests
from typing import List
from google import genai
from google.genai import types
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

def obtener_modelo_embeddings():
#    """
#    Inicializa el modelo de embeddings de Google GenAI.
#    Este modelo transforma texto en vectores de 768 dimensiones.
#    Es gratuito dentro de las cuotas del plan estándar de Google AI Studio.
#    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY no encontrada en las variables de entorno.")

    return GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=api_key,
        google_api_gateway="https://generativelanguage.googleapis.com/v1"
    )
