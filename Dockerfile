# 1. Imagen base de Python
FROM python:3.11-slim

# 2. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar dependencias
COPY requirements.txt .

# 4. Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del proyecto
COPY . .

# 6. Exponer el puerto (FastAPI usa 8000 por defecto)
EXPOSE 8000

# 7. Comando que arranca tu API
CMD ["uvicorn", "api_agente:app", "--host", "0.0.0.0", "--port", "8000"]
