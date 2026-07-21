# api_agente.py

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# === Middleware CORS ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Permite cualquier origen
    allow_credentials=True,
    allow_methods=["*"],        # Permite todos los métodos
    allow_headers=["*"],        # Permite todos los encabezados
)

# === Endpoints básicos ===
@app.get("/")
def root():
    return {"message": "Agente IA funcionando en Colab con autenticación automática"}

@app.post("/subir-pdf")
async def subir_pdf(file: UploadFile = File(...)):
    return {"filename": file.filename, "status": "PDF recibido"}

@app.post("/consultar-csv")
async def consultar_csv(file: UploadFile = File(...)):
    return {"filename": file.filename, "status": "CSV recibido"}

@app.post("/consultar-gemini")
async def consultar_gemini(pregunta: str):
    return {"pregunta": pregunta, "respuesta": "Respuesta simulada del agente IA"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
