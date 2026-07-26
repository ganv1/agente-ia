# api_agente.py

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
import pandas as pd

app = FastAPI()

# 👉 Servir el index.html como página principal
@app.get("/")
def read_root():
    return FileResponse("index.html")

# 👉 Endpoint para subir PDF
@app.post("/subir-pdf")
async def subir_pdf(file: UploadFile = File(...)):
    # Aquí podrías procesar el PDF (ejemplo: guardarlo temporalmente)
    content = await file.read()
    # Simulación de respuesta
    return {"filename": file.filename, "status": "PDF recibido correctamente"}

# 👉 Endpoint para consultar CSV
@app.post("/consultar-csv")
async def consultar_csv(query: dict):
    # Ejemplo: simular que tienes un CSV cargado
    # En producción, deberías leer un archivo real
    data = {
        "Nombre": ["Ana", "Luis", "Pedro"],
        "Edad": [25, 30, 40]
    }
    df = pd.DataFrame(data)

    # Simulación: devolver todo el dataset si se pide "todos"
    if query.get("query") == "todos":
        return df.to_dict(orient="records")
    else:
        return {"resultado": f"Consulta recibida: {query.get('query')}"}

# 👉 Endpoint para consultar Gemini
@app.post("/consultar-gemini")
async def consultar_gemini(pregunta: dict):
    # Aquí iría la integración real con Gemini
    # Simulación de respuesta
    return {"respuesta": f"Gemini procesó la pregunta: {pregunta.get('pregunta')}"}
