# Usa una imagen base oficial de Python como imagen base
FROM python:3.12-slim

# Establece el directorio de trabajo en /twilio
WORKDIR /twilio

# Copia el archivo de requisitos en el directorio de trabajo
COPY requirements.txt .

# Instala las dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    pkg-config

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido de tu aplicación en el directorio de trabajo
COPY . .

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
