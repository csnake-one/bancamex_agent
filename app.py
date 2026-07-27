import os
import streamlit as st
from agent.graph import (
    construir_grafo,
)  # Ajusta según tu función principal en graph.py

# Configuración de la página
st.set_page_config(
    page_title="Agente RAG - Banca-Mex", page_icon="🏦", layout="centered"
)

st.title("🏦 Asistente Virtual Banca-Mex")
st.write(
    "Pregúntame sobre políticas, costos y condiciones de servicio de Banca-Mex."
)

# Inicializar el historial de chat en la sesión de Streamlit
app_agente = construir_grafo()
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes anteriores al recargar la página
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capturar la entrada del usuario
if prompt := st.chat_input("¿En qué puedo ayudarte hoy?"):
    # Agregar mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar respuesta del agente RAG
    with st.chat_message("assistant"):
        with st.spinner("Consultando políticas de Banca-Mex..."):
            try:
                # Aquí llamas a tu lógica de LangChain / RAG definida en agent/graph.py
                #respuesta = invocar_agente(prompt)
                inputs = {"pregunta": prompt}
                respuesta = app_agente.invoke(inputs)
            except Exception as e:
                respuesta = f"Ocurrió un error al procesar tu solicitud: {e}"

            st.markdown(respuesta['respuesta'])

    # Agregar respuesta al historial
    st.session_state.messages.append({"role": "assistant", "content": respuesta['respuesta']})
