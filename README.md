# bancamex_agent
Proyecto que pretende crear un agente que pueda responder las preguntas de los usuarios de la fintech BancaMex (empresa ficticia). Challenge para entregar en G10 de aluralatam
El agente respondera de forma exclusiva preguntas relacionadas con la empresa Banca-Mex como por ejemplo:
 - Condiciones comerciales
 - Tarifas y comisiones por los servicios
 - Politicas de los servicios
 - Descricpion y ubicacion de la empresa

# Agente de Consultas - Banca Mex
## Estructura

Este proyecto contiene el agente inteligente basado en arquitecturas RAG utilizando LangGraph y Gemini para responder consultas estrictamente limitadas a las políticas internas de Banca-Mex.
Se utilizo ChromaDB para la almacenar los vectores de informacion y estos sean utilizados por GEMINI para poder responder de manera exlusiva las preguntas sobre Banca-Mex.
Este proyecto sigue un diseño modular dividiendo la base de datos de vectores (`ChromaDB`), la orquestación del agente (`LangGraph`) y las interfaces de ejecución:

bancamex-agent/
│

├── data/

     │

     └── politicas_bancamex.txt   # Documentación oficial de la banca

├── agent/

        │

        └── database.py             #Ingesta y conexion a la BD que en este caso se opta por ChromaDB
        
│    └── embeddings.py           #Configuracion del modelo de embeddings

│    └── graph.py                #llamadas a Gemini y logica de LangChain

│    └──prompts.py             #prompts para establecer las funciones y establecer limites con guardrails

|

├── chroma_db/                  # Carpeta donde se guardará la BD vectorial

│

├── .env                        # Variables de entorno (Ignorado en Git)

├── .gitignore                  # Archivos ignorados por Git

├── README.md                   # Documentación del repositorio

├── requirements.txt            # Dependencias del proyecto

│

└── main.py                     #Programa principal y base del agente


El flujo que sigue y como se orquestan las herramientas es la siguiente:



                [Usuario: Pregunta] 
                       │
                       ▼
                [Nodo: Recuperar Contexto (ChromaDB)] 
                       │
                       ▼
                [Nodo: Generar Respuesta (Gemini + Prompts con Guardrails)]
                       │
                       ▼
                [Validación / Guardrail] ──(¿Tiene relación con Banca Mex?)──► [No] ──► Respuesta Genérica de Bloqueo
                       │ [Sí]
                       ▼
                [Respuesta Final al Usuario]


## Herramientas utilizadas

1. python 3.13
2. Langraph
3. Gemini
4. ChromaDB
5. streamlit

## Ejecución rápida
1. Configure su entorno local e instale las dependencias de requirements.txt
2. Inserte su `GOOGLE_API_KEY` en el archivo `.env`.
3. Ejecute `python main.py` para interactuar con el agente por consola.
4. Ejecute `streamlit run app.py` para poder interactuar de manera grafica y via web con su navegador por defecto
5. Puede probar su funcionamiento en la siguiente direccion: https://bancamexagent-alura-one10.streamlit.app/

## Ejemplos de preguntas que el agente puede responder

 1. ¿Que es Banca Mex?
 2. ¿Donde se ubica Banca Mex?
 3. ¿Que sericios ofrece Banca Mex?
 4. ¿Tiene comisiones Banca Mex?
 
## Ejemplos de respuestas que el agente genera

 1. Banca Mex es una institucion de fondos de pago Electronico (IFPE) que opera en cumplimiento con la Ley para Regular las Instituciones de Tecnologia Financiera.
    (Ley Fintech)
    
 2. Lo siento como asesor de Banca Mex, solo puedo resolver dudas relacionadas con nuestras politicas y servicios oficiales documentados
 
## Imagen de la pagina web corriendo la aplicacion

<img width="1843" height="988" alt="imagen" src="https://github.com/user-attachments/assets/ae761b6a-2a70-4193-aba7-705a742e2303" />

