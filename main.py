#Programa principal y base del agente

from agent.graph import construir_grafo
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    if not os.getenv("GOOGLE_API_KEY"):
        print("[ERROR] Por favor, configura tu GOOGLE_API_KEY en el archivo .env")
        return

    print("====================================================")
    print("  Agente de Políticas Internas de Banca Mex Inicializado")
    print("====================================================")
    print("Escribe 'salir' para terminar el chat.\n")

    # Compilar el grafo de LangGraph
    app_agente = construir_grafo()

    while True:
        usuario_input = input("Usuario: ")
        if usuario_input.strip().lower() == "salir":
            print("Chat finalizado. ¡Hasta luego!")
            break

        if not usuario_input.strip():
            continue

        # Ejecución del grafo pasando el estado inicial
        inputs = {"pregunta": usuario_input}
        resultado = app_agente.invoke(inputs)

        print(f"Agente BancaMex: {resultado['respuesta']}\n")

if __name__ == "__main__":
    main()
