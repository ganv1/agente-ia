# api_agente.py

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
import pdfplumber
import os
import google.generativeai as genai

app = FastAPI()

# Configura Gemini con tu API Key desde variable de entorno
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

PDF_PATH = "archivo.pdf"

@app.get("/")
def read_root():
    # Sirve el frontend principal
    return FileResponse("index.html")

@app.post("/subir-pdf")
async def subir_pdf(file: UploadFile = File(...)):
    try:
        with open(PDF_PATH, "wb") as f:
            f.write(await file.read())
        return {"filename": file.filename, "status": "✅ PDF guardado correctamente"}
    except Exception as e:
        return JSONResponse(content={"error": f"Error al guardar el PDF: {str(e)}"}, status_code=500)

@app.post("/consultar-csv")
async def consultar_csv(query: dict):
    consulta = query.get("query", "")
    return {"resultado": f"Consulta recibida: {consulta}"}

@app.post("/consultar-gemini")
async def consultar_gemini(pregunta: dict):
    texto_pregunta = pregunta.get("pregunta", "")

    if not os.path.exists(PDF_PATH):
        return JSONResponse(content={"error": "⚠️ No se ha subido ningún PDF"}, status_code=400)

    # Extraer texto del PDF
    contenido_texto = ""
    try:
        with pdfplumber.open(PDF_PATH) as pdf:
            for pagina in pdf.pages:
                contenido_texto += pagina.extract_text() or ""
    except Exception as e:
        return JSONResponse(content={"error": f"Error al leer el PDF: {str(e)}"}, status_code=500)

    if not contenido_texto.strip():
        return {"error": "⚠️ El PDF no contiene texto"}

    # Llamar a Gemini para generar resumen
    try:
        modelo = genai.GenerativeModel("gemini-pro")  # modelo estable
        prompt = (
            f"Resume el siguiente documento en no más de 7 líneas, "
            f"de forma clara y concisa:\n\n{contenido_texto[:4000]}"
        )
        respuesta = modelo.generate_content(prompt)
        resumen = respuesta.text.strip() if respuesta.text else "No se obtuvo respuesta del modelo."
        return {"respuesta": resumen}
    except Exception as e:
        return JSONResponse(content={"error": f"Error al consultar Gemini: {str(e)}"}, status_code=500)
