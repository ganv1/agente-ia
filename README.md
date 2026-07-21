# 🚀 Agente IA con FastAPI y Frontend

Este proyecto implementa un **Agente de Inteligencia Artificial** capaz de:
1. Procesar documentos PDF y CSV.
2. Responder preguntas sobre el contenido de los documentos.
3. Exponerse públicamente mediante despliegue en la nube (Render, Oracle Cloud, etc.).

---

## 📂 Estructura del proyecto
- `api_agente.py` → Backend con FastAPI y endpoints:
  - `/` → mensaje de bienvenida
  - `/subir-pdf` → subir y procesar PDF
  - `/consultar-csv` → subir y procesar CSV
  - `/consultar-gemini` → responder preguntas
- `index.html` → Frontend simple para interactuar con el agente.
- `requirements.txt` → dependencias necesarias.
- `Dockerfile` → configuración para despliegue en contenedor.

---

## ⚙️ Instalación local

1. Clona el repositorio:
   ```bash
   git clone https://github.com/ganv1/agente-ia.git
   cd agente-ia

2. Instalacion de dependencias:
    pip install -r requirements.txt

3. Ejecuta el servidor:
   uvicorn api_agente:app --host 0.0.0.0 --port 8000

4. Abre el frontend:
   python -m http.server 5500

Luego visita: http://127.0.0.1:5500/index.html
