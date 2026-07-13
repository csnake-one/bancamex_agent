#Ingesta y conexion a la BD que en este caso se opta por ChromaDB

import os
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from agent.embeddings import obtener_modelo_embeddings

DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma_db")
FILE_PATH = os.getenv("POLITICAS_FILE_PATH", "./data/politicas_bancamex.txt")

def inicializar_o_cargar_db():
    """
    Verifica si la base de datos vectorial existe. Si no, lee el archivo de políticas,
    lo fragmenta (chunking), genera los embeddings y los almacena en ChromaDB.
    """
    embeddings = obtener_modelo_embeddings()

    # Si la carpeta chroma_db existe y tiene archivos, asumimos que ya está indexada
    if os.path.exists(DB_PATH) and len(os.listdir(DB_PATH)) > 0:
        print("[INFO] Cargando base de datos vectorial persistente desde disk...")
        vector_store = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
        return vector_store.as_retriever(search_kwargs={"k": 2})

    print("[INFO] Base de datos no encontrada. Iniciando proceso de ingesta...")
    if not os.path.exists(FILE_PATH):
        raise FileNotFoundError(f"No se encontró el archivo de políticas en {FILE_PATH}")

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Fragmentamos el texto para que la búsqueda sea más precisa
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
    fragmentos = text_splitter.create_documents([contenido])

    # Creación y persistencia en ChromaDB
    vector_store = Chroma.from_documents(
        documents=fragmentos,
        embedding=embeddings,
        persist_directory=DB_PATH
    )
    print("[INFO] Ingesta completada con éxito y persistida en disco.")
    return vector_store.as_retriever(search_kwargs={"k": 2})
