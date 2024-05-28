# Usa una imagen base oficial de Python 3.12
FROM python:3.12-slim

# Establece el directorio de trabajo en /app
WORKDIR /twilio

# Copia los archivos requirements.txt y .env.example en el directorio de trabajo
COPY requirements.txt ./
COPY .env.example ./.env

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación en el directorio de trabajo
COPY . .

# Expone el puerto 8000 para la aplicación FastAPI
EXPOSE 8000

# Comando para ejecutar las migraciones de la base de datos
RUN alembic upgrade head

# Comando para iniciar la aplicación
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8000"]
