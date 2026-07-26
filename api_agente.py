# api_agente.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
import pdfplumber
import os
import google.generativeai as genai

app = FastAPI()

# Configura Gemini con tu API Key desde variable de entorno
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

DOCS_DIR = "docs"

@app.get("/")
def read_root():
    # Sirve el frontend principal
    return FileResponse("index.html")

@app.post("/subir-pdf")
async def subir_pdf(file: UploadFile = File(...)):
    try:
        # Crear carpeta docs si no existe
        os.makedirs(DOCS_DIR, exist_ok=True)

        # Guardar el archivo con su nombre original dentro de docs/
        file_path = os.path.join(DOCS_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())

        return {
            "filename": file.filename,
            "status": "✅ Archivo guardado correctamente en carpeta docs/"
        }
    except Exception as e:
        return JSONResponse(
            content={"error": f"Error al guardar el archivo: {str(e)}"},
            status_code=500
        )
