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
        os.makedirs(DOCS_DIR, exist_ok=True)
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

@app.post("/consultar-gemini")
async def consultar_gemini(pregunta: dict):
    nombre_archivo = pregunta.get("archivo", "")
    texto_pregunta = pregunta.get("pregunta", "")

    if not nombre_archivo:
        return JSONResponse(
            content={"error": "⚠️ Debes indicar el nombre del archivo"},
            status_code=400
        )

    file_path = os.path.join(DOCS_DIR, nombre_archivo)
    if not os.path.exists(file_path):
        return JSONResponse(
            content={"error": f"⚠️ El archivo {nombre_archivo} no existe"},
            status_code=404
        )

    # Extraer texto del PDF
    contenido_texto = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for pagina in pdf.pages:
                contenido_texto += pagina.extract_text() or ""
    except Exception as e:
        return JSONResponse(
            content={"error": f"Error al leer el PDF: {str(e)}"},
            status_code=500
        )

    if not contenido_texto.strip():
        return {"error": "⚠️ El PDF no contiene texto"}

    # Llamar a Gemini
    try:
        modelo = genai.GenerativeModel("models/gemini-2.5-flash")
        prompt = (
            f"Resume el documento '{nombre_archivo}' en no más de 7 líneas, "
            f"de forma clara y concisa:\n\n{contenido_texto[:4000]}"
        )
        respuesta = modelo.generate_content(prompt)
        resumen = respuesta.text.strip() if respuesta.text else "No se obtuvo respuesta del modelo."
        return {"archivo": nombre_archivo, "respuesta": resumen}
    except Exception as e:
        return JSONResponse(
            content={"error": f"Error al consultar Gemini: {str(e)}"},
            status_code=500
        )
