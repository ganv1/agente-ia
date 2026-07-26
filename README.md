# 📄 Agente IA Documentos con FastAPI + Gemini

## 👤 Autor
**Alberto Neira**  
Analista de Sistemas, Consultor TI y Data Science

---

## 📌 Descripción
Este proyecto implementa un agente IA que permite:
- Subir documentos PDF y CSV.
- Consultar y resumir documentos usando **Google Gemini**.
- Interactuar mediante un frontend simple en HTML.
- Deploy en la nube con **Render**.

---

## 🏗️ Arquitectura
- **FastAPI**: Backend con endpoints `/subir-pdf`, `/consultar-gemini`, etc.
- **pdfplumber**: Extracción de texto desde PDFs.
- **Google Generative AI SDK**: Conexión con modelos Gemini (`models/gemini-2.5-flash`).
- **Frontend HTML**: Interfaz para subir archivos y consultar resúmenes.
- **Render**: Deploy en la nube.

---

## 🚀 Ejecución local
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/TUUSUARIO/agente-ia.git
   cd agente-ia

2. Instalar dependencias:
   pip install -r requirements.txt

3. Configurar tu API Key:
   export GOOGLE_API_KEY="TU_API_KEY"

4. Ejecutar FastAPI:
   uvicorn api_agente:app --reload

5. Abrir en navegador:
http://127.0.0.1:8000 

Ejemplos de uso
Subir archivo:  
Selecciona un PDF en el formulario y súbelo.

Consultar resumen:  
Elige el archivo en el menú desplegable y escribe:

Resume este documento en 7 líneas
Muestra los puntos mas importantes del documento

Obtendrás una respuesta generada por Gemini.

Deploy en Render
Enlace al servicio: https://tu-deploy-render.onrender.com (tu-deploy-render.onrender.com in Bing)

Captura de pantalla incluida en la carpeta /docs/screenshots.


📜 Historial de commits
El repositorio incluye commits organizados que muestran:

Configuración inicial.

Integración con Gemini.

Manejo de múltiples documentos.

Frontend con menú desplegable.

Deploy en Render.

📂 Estructura del repositorio

agente-ia/
├── api_agente.py
├── index.html
├── requirements.txt
├── Dockerfile
├── README.md
└── docs/   (carpeta donde se guardan los PDFs/CSV)
