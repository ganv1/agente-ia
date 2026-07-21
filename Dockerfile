# Imagen base ligera de Python
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# requirements.txt para aprovechar cache de Docker
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del proyecto
COPY . .

# Exponemos el puerto 8000 (FastAPI)
EXPOSE 8000

# Comando de arranque del servidor
CMD ["uvicorn", "api_agente:app", "--host", "0.0.0.0", "--port", "8000"]
