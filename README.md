# Twilio Backend
Este proyecto es un backend desarrollado en Python con FastAPI y Twilio para enviar mensajes de WhatsApp y programar recordatorios de eventos.

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Configuración](#configuración)
- [Scripts Disponibles](#scripts-disponibles)
- [Licencia](#licencia)

## Requisitos
Para el sigente proyectose requierede las siguentes herramientas:
1. Python 3.12 - para la instalación de python por favor revisa la [documentación oficial](https://www.python.org/downloads/)
2. pip - para la instalación de pip por favor revisa la [documentación oficial](https://pip.pypa.io/en/stable/installation/)
3. Twilio - para obtener twilio con whatsapp por favor revisa la [documentación oficial](https://www.twilio.com/docs/whatsapp/quickstart/python)
4. git - para la instalación de git por favor revisa la [documentación oficial](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) y escoge tu sistema operativo.
5. Visual Studio Code - para la instalación de Visual Studio Code por favor revisa la [documentación oficial](https://code.visualstudio.com/download) y escoge tu sistema operativo.

## Instalación

Instrucciones para instalar el proyecto.

1. Primero clona el repositorio.
```bash
git clone https://github.com/AcceptGO-Projects/twilio-backend.git
```

2. instala las dependencias del proyecto.
```bash
pip install -r requirements.txt
```

## Uso
Instrucciones básicas de uso del proyecto.

``` bash
uvicorn app.main:app --reload
```

### Uso de Docker Compose para pruebas locales
Para ejecutar el proyecto en un contenedor de Docker, puedes usar Docker Compose. El archivo `docker-compose.yml` contiene la configuración necesaria para ejecutar el proyecto en un contenedor de Docker.

```bash
docker-compose up
```

## Estructura del Proyecto
```bash
│   .env.example
│   .gitignore
│   alembic.ini
│   alembic_explanation.md
│   code_explanation.md
│   docker-compose.yml
│   Dockerfile
│   example_receive_message.py
│   example_send_message.py
│   Procfile
│   requirements.txt
│   tree.txt
│
├───alembic
│       env.py
│       README
│       script.py.mako
│
├───app
│   │   main.py
│   │
│   ├───api
│   │       event_controller.py
│   │       lead_controller.py
│   │       message_controller.py
│   │       router.py
│   │
│   ├───config
│   │       config.py
│   │       data_source.py
│   │
│   ├───helpers
│   │       date_formater.py
│   │       reminder_factory.py
│   │
│   ├───models
│   │       base.py
│   │       event.py
│   │       event_reminder.py
│   │       lead.py
│   │       lead_event.py
│   │       message.py
│   │       reminder.py
│   │       __init__.py
│   │
│   ├───repositories
│   │       evente_reminder_repository.py
│   │       event_repository.py
│   │       lead_event_repository.py
│   │       lead_repository.py
│   │       message_repository.py
│   │       reminder_repository.py
│   │       __init__.py
│   │
│   ├───schemas
│   │       event_reminder_schema.py
│   │       lead.py
│   │       lead_reminder_response.py
│   │       lead_response.py
│   │       message.py
│   │
│   ├───services
│   │       lead_service.py
│   │       message_service.py
│   │       scheduler_service.py
│   │       twilio_service.py
│   │
│   └───templates
│           messages_templates.py
│
└───__pycache__
        dependencies.cpython-311.pyc
        main.cpython-311.pyc
```

- Para la explicación de la estructura del proyecto de la carpeta app por favor revisa el archivo -> [code_explanation.md](code_explanation.md)
- Para la explicación de la estructura del proyecto de la carpeta alembic por favor revisa el archivo -> [alembic_explanation.md](alembic_explanation.md)

## Configuración

### Archivos de Configuración

- **`alembic.ini`**: Archivo de configuración principal para Alembic, contiene la configuración necesaria para ejecutar migraciones de base de datos.
  - Parámetros principales:
    - `script_location`: Ubicación de los scripts de Alembic.
    - `sqlalchemy.url`: URL de la base de datos.

### Archivo [`.env.example`](./.env.example)

Este archivo proporciona un ejemplo de las variables de entorno necesarias para la configuración del proyecto. Copia este archivo y renómbralo a `.env`, luego llena los valores correspondientes.

```env
# Configuración de Twilio
TWILIO_AUTH_TOKEN=tu_token_de_auth_de_twilio
TWILIO_ACCOUNT_SSID=tu_ssid_de_twilio
TWILIO_NUMBER=tu_numero_de_twilio

# URL de la base de datos
DATABASE_URL=sqlite:///./test.db

# Otros parámetros de configuración
SERVICE_NAME=Backend Python FastAPI and Twilio
K_REVISION=local
LOG_LEVEL=DEBUG
```

## Scripts Disponibles

### [`example_receive_message.py`](./example_receive_message.py)
Este script configura un servidor Flask para recibir y responder mensajes de WhatsApp utilizando Twilio.

- **Descripción:**
  - Configura una ruta `/whatsapp` para recibir mensajes de WhatsApp.
  - Responde automáticamente a los mensajes que contienen la palabra "hola".

- **Uso:**
  - Ejecuta el script para iniciar el servidor Flask:
    ```bash
    python example_receive_message.py
    ```
  - Envía un mensaje de WhatsApp al número configurado para recibir una respuesta automática.

### [`example_send_message.py`](./example_send_message.py)
Este script envía mensajes de WhatsApp a una lista de números utilizando Twilio.

- **Descripción:**
  - Define una lista de números de teléfono.
  - Envía un mensaje de WhatsApp a cada número en la lista utilizando la API de Twilio.

- **Uso:**
  - Configura `account_sid` y `auth_token` con tus credenciales de Twilio.
  - Ejecuta el script para enviar mensajes a los números configurados:
    ```bash
    python example_send_message.py
    ```