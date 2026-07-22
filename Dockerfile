FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Actualiza pip y setuptools antes de instalar dependencias
RUN pip install --upgrade pip setuptools wheel

# Instala dependencias sin cache
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api_agente:app", "--host", "0.0.0.0", "--port", "8000"]

