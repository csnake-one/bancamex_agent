#Configuracion del modelo de embeddings

import os
from langchain_google_genai import GoogleGenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def obtener_modelo_embeddings():
    """
    Inicializa el modelo de embeddings de Google GenAI.
    Este modelo transforma texto en vectores de 768 dimensiones.
    Es gratuito dentro de las cuotas del plan estándar de Google AI Studio.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY no encontrada en las variables de entorno.")

    return GoogleGenAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=api_key
    )
