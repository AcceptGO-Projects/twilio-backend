# Explicación del Código en la Carpeta `app`
## Documentación de Controladores en `app/api`
### [`event_controller.py`](./app/api/event_controller.py)
Este archivo define las rutas y manejadores de eventos.

- **Ruta:** `/events`
- **Método:** `POST`
- **Descripción:** Crea un nuevo evento y sus recordatorios asociados.
- **Esquema de solicitud:** `CreateEventRequest`
- **Código de estado:** `201 CREATED`

### [`lead_controller.py`](./app/api/lead_controller.py)
Este archivo gestiona las operaciones relacionadas con los leads.

- **Rutas y Métodos:**
  - **`/register` (POST):** Registra un nuevo lead.
  - **`/` (GET):** Obtiene todos los leads con eventos asociados.
  - **`/event/{event_id}` (GET):** Obtiene los leads asociados a un evento específico.
  - **`/reminders/status` (GET):** Obtiene los estados de los recordatorios de leads.

### [`message_controller.py`](./app/api/message_controller.py)
Este archivo gestiona las operaciones relacionadas con los mensajes.

- **Rutas y Métodos:**
  - **`/messages` (GET):** Obtiene todos los mensajes.
  - **`/messages/{message_id}` (GET):** Obtiene un mensaje específico por su ID.

### [`router.py`](./app/api/router.py)
Este archivo configura los enrutadores de la API, agrupando los controladores específicos bajo prefijos y etiquetas comunes.

- **Descripción:**
  - **Prefijo:** `/leads`
  - **Tags:** `leads`
  - **Prefijo:** `/messages`
  - **Tags:** `messages`
  - **Prefijo:** `/events`
  - **Tags:** `events`

## Documentación de Configuración en `app/config`

### [`config.py`](./app/config/config.py)
Este archivo define las configuraciones básicas de la aplicación utilizando Pydantic.

- **Clase:** `Settings`
  - **Atributos:**
    - `service_name` (str): Nombre del servicio.
    - `k_revision` (str): Revisión del servicio, por defecto "local".
    - `log_level` (str): Nivel de log, por defecto "DEBUG".
    - `twilio_auth_token` (str): Token de autenticación de Twilio.
    - `twilio_account_ssid` (str): SSID de la cuenta de Twilio.
    - `twilio_number` (str): Número de Twilio.
    - `database_url` (str): URL de la base de datos.

- **Configuración de entorno:**
  - El archivo de configuración `.env` es utilizado para cargar las variables de entorno.
  - Puedes modificar las variables de entorno en el archivo [`aqui`](./.env.example).

- **Función:**
  - `get_settings()`: Función cacheada que retorna la configuración.

### [`data_source.py`](./app/config/data_source.py)
Este archivo configura la conexión a la base de datos y define la función para obtener la sesión de la base de datos.

- **Constantes:**
  - `DATABASE_URL` (str): URL de la base de datos, obtenida desde las configuraciones.

- **Motor de base de datos:**
  - `engine`: Crea el motor de base de datos asíncrono utilizando `create_async_engine`.

- **Sesión de base de datos:**
  - `AsyncSessionLocal`: Configura la sesión de base de datos asíncrona utilizando `sessionmaker`.

- **Funciones:**
  - `create_tables()`: Crea las tablas en la base de datos si no existen.
  - `get_db()`: Generador asíncrono que maneja la sesión de la base de datos.

## Documentación de Modelos en `app/helpers`

### [`date_formater.py`](./app/helpers/date_formater.py)
Este archivo contiene funciones para el formateo de fechas.

- **Funciones:**
  - `format_date_to_spanish_utc4(date_utc0: datetime) -> str`: 
    - **Descripción:** Esta función toma una fecha en UTC+0 y la convierte a UTC-4, formateándola en español.
    - **Entrada:** `date_utc0` (datetime): La fecha en UTC+0.
    - **Salida:** (str): La fecha formateada en español, incluyendo el día de la semana y el mes en palabras.

### [`reminder_factory.py`](./app/helpers/reminder_factory.py)
Este archivo contiene funciones para la manipulación de mensajes de recordatorio.

- **Funciones:**
  - `replace_message_with_name(message: str, name: str) -> str`:
    - **Descripción:** Esta función reemplaza un marcador de posición (`{{name}}`) en un mensaje con un nombre específico.
    - **Entrada:** 
      - `message` (str): El mensaje que contiene el marcador de posición.
      - `name` (str): El nombre que reemplazará el marcador de posición.
    - **Salida:** (str): El mensaje con el nombre reemplazado.

## Documentación de Modelos en `app/models`

### [`base.py`](./app/models/base.py)
Este archivo define la base común para todos los modelos de SQLAlchemy en la aplicación.

- **Descripción:** 
  - Define `Base` utilizando `declarative_base()` de SQLAlchemy, que sirve como la clase base para todos los modelos de la base de datos.

### [`event.py`](./app/models/event.py)
Este archivo define el modelo para los eventos.

- **Tabla:** `events`
- **Atributos:**
  - `id` (Integer): Identificador único del evento.
  - `name` (String): Nombre del evento.
  - `description` (String): Descripción del evento.
  - `event_date` (DateTime): Fecha del evento.
  - `created_at` (DateTime): Fecha de creación del registro, por defecto la fecha y hora actual.
- **Relaciones:**
  - `leads`: Relación con la tabla `LeadEvent`.
  - `reminders`: Relación con la tabla `EventReminder`.

### [`event_reminder.py`](./app/models/event_reminder.py)
Este archivo define el modelo para los recordatorios de eventos.

- **Tabla:** `event_reminders`
- **Atributos:**
  - `id` (Integer): Identificador único del recordatorio.
  - `event_id` (Integer): Identificador del evento asociado.
  - `index` (Integer): Índice del recordatorio.
  - `message` (String): Mensaje del recordatorio.
  - `reminder_time` (DateTime): Fecha y hora del recordatorio.
- **Relaciones:**
  - `event`: Relación con la tabla `Event`.

### [`lead.py`](./app/models/lead.py)
Este archivo define el modelo para los leads.

- **Tabla:** `leads`
- **Atributos:**
  - `id` (Integer): Identificador único del lead.
  - `first_name` (String): Nombre del lead.
  - `last_name` (String): Apellido del lead.
  - `email` (String): Correo electrónico del lead.
  - `country` (String): País del lead.
  - `phone` (String): Número de teléfono del lead.
- **Relaciones:**
  - `events`: Relación con la tabla `LeadEvent`.

### [`lead_event.py`](./app/models/lead_event.py)
Este archivo define el modelo para la relación entre leads y eventos.

- **Tabla:** `lead_events`
- **Atributos:**
  - `id` (Integer): Identificador único de la relación.
  - `lead_id` (Integer): Identificador del lead asociado.
  - `event_id` (Integer): Identificador del evento asociado.
  - `registered_at` (DateTime): Fecha y hora de registro de la relación.
- **Relaciones:**
  - `lead`: Relación con la tabla `Lead`.
  - `event`: Relación con la tabla `Event`.
  - `reminders`: Relación con la tabla `Reminder`.

### [`message.py`](./app/models/message.py)
Este archivo define el modelo para los mensajes.

- **Tabla:** `messages`
- **Atributos:**
  - `id` (Integer): Identificador único del mensaje.
  - `recipient` (String): Destinatario del mensaje.
  - `content` (String): Contenido del mensaje.
  - `sent_at` (DateTime): Fecha y hora de envío del mensaje.
  - `is_successful` (Boolean): Indica si el envío fue exitoso.
  - `error_message` (String, nullable=True): Mensaje de error si el envío falló.

### [`reminder.py`](./app/models/reminder.py)
Este archivo define el modelo para los recordatorios.

- **Tabla:** `reminders`
- **Atributos:**
  - `id` (Integer): Identificador único del recordatorio.
  - `lead_event_id` (Integer): Identificador de la relación `LeadEvent` asociada.
  - `to_number` (String): Número de teléfono al que se enviará el recordatorio.
  - `content` (String): Contenido del recordatorio.
  - `reminder_date` (DateTime): Fecha y hora del recordatorio.
  - `sent` (Boolean): Indica si el recordatorio ha sido enviado.
- **Relaciones:**
  - `lead_event`: Relación con la tabla `LeadEvent`.

## Documentación de Repositorios en `app/repositories`

### [`event_repository.py`](./app/repositories/event_repository.py)
Este archivo gestiona las operaciones relacionadas con los eventos en la base de datos.

- **Funciones:**
  - `add_event(new_event: Event) -> Event`:
    - **Descripción:** Añade un nuevo evento a la base de datos.
    - **Entrada:** `new_event` (Event): El evento a añadir.
    - **Salida:** (Event): El evento añadido.
  - `get_event_by_id(event_id: int) -> Event`:
    - **Descripción:** Obtiene un evento por su ID.
    - **Entrada:** `event_id` (int): El ID del evento.
    - **Salida:** (Event): El evento correspondiente al ID.

### [`evente_reminder_repository.py`](./app/repositories/evente_reminder_repository.py)
Este archivo gestiona las operaciones relacionadas con los recordatorios de eventos en la base de datos.

- **Funciones:**
  - `get_welcome_message_by_event_id(event_id: int) -> EventReminder`:
    - **Descripción:** Obtiene el mensaje de bienvenida para un evento específico.
    - **Entrada:** `event_id` (int): El ID del evento.
    - **Salida:** (EventReminder): El recordatorio de bienvenida.
  - `get_reminders_by_event_id(event_id: int) -> List[EventReminder]`:
    - **Descripción:** Obtiene todos los recordatorios para un evento específico, excluyendo el mensaje de bienvenida.
    - **Entrada:** `event_id` (int): El ID del evento.
    - **Salida:** (List[EventReminder]): La lista de recordatorios.

### [`lead_event_repository.py`](./app/repositories/lead_event_repository.py)
Este archivo gestiona las operaciones relacionadas con la relación entre leads y eventos en la base de datos.

- **Funciones:**
  - `add_lead_event(new_lead_event: LeadEvent) -> LeadEvent`:
    - **Descripción:** Añade una nueva relación lead-event a la base de datos.
    - **Entrada:** `new_lead_event` (LeadEvent): La relación lead-event a añadir.
    - **Salida:** (LeadEvent): La relación añadida.

### [`lead_repository.py`](./app/repositories/lead_repository.py)
Este archivo gestiona las operaciones relacionadas con los leads en la base de datos.

- **Funciones:**
  - `add_lead(new_lead: Lead) -> Lead`:
    - **Descripción:** Añade un nuevo lead a la base de datos.
    - **Entrada:** `new_lead` (Lead): El lead a añadir.
    - **Salida:** (Lead): El lead añadido.
  - `find_lead_by_email_or_phone(email: str, phone: str) -> Lead`:
    - **Descripción:** Busca un lead por su correo electrónico o número de teléfono.
    - **Entrada:** `email` (str): El correo electrónico del lead.
    - **Entrada:** `phone` (str): El número de teléfono del lead.
    - **Salida:** (Lead): El lead encontrado.
  - `get_all_leads_with_events()`:
    - **Descripción:** Obtiene todos los leads con sus eventos asociados.
    - **Salida:** (list[Lead]): La lista de leads con eventos.
  - `get_leads_by_event(event_id: int)`:
    - **Descripción:** Obtiene todos los leads asociados a un evento específico.
    - **Entrada:** `event_id` (int): El ID del evento.
    - **Salida:** (list[Lead]): La lista de leads asociados al evento.
  - `get_lead_reminder_status()`:
    - **Descripción:** Obtiene el estado de los recordatorios de los leads.
    - **Salida:** (list[dict]): La lista de estados de recordatorios.

### [`message_repository.py`](./app/repositories/message_repository.py)
Este archivo gestiona las operaciones relacionadas con los mensajes en la base de datos.

- **Funciones:**
  - `add_message(recipient: str, content: str, is_successful: bool, error_message: str = "") -> Message`:
    - **Descripción:** Añade un nuevo mensaje a la base de datos.
    - **Entrada:** `recipient` (str): El destinatario del mensaje.
    - **Entrada:** `content` (str): El contenido del mensaje.
    - **Entrada:** `is_successful` (bool): Indica si el mensaje fue enviado exitosamente.
    - **Entrada:** `error_message` (str, opcional): Mensaje de error si el envío falló.
    - **Salida:** (Message): El mensaje añadido.
  - `get_messages()`:
    - **Descripción:** Obtiene todos los mensajes.
    - **Salida:** (list[Message]): La lista de mensajes.
  - `get_message_by_id(message_id: int) -> Message`:
    - **Descripción:** Obtiene un mensaje por su ID.
    - **Entrada:** `message_id` (int): El ID del mensaje.
    - **Salida:** (Message): El mensaje correspondiente al ID.

### [`reminder_repository.py`](./app/repositories/reminder_repository.py)
Este archivo gestiona las operaciones relacionadas con los recordatorios en la base de datos.

- **Funciones:**
  - `add_reminder(lead_event_id: int, to_number: str, content: str, reminder_date: datetime) -> Reminder`:
    - **Descripción:** Añade un nuevo recordatorio a la base de datos.
    - **Entrada:** `lead_event_id` (int): El ID de la relación lead-event asociada.
    - **Entrada:** `to_number` (str): El número de teléfono al que se enviará el recordatorio.
    - **Entrada:** `content` (str): El contenido del recordatorio.
    - **Entrada:** `reminder_date` (datetime): La fecha y hora del recordatorio.
    - **Salida:** (Reminder): El recordatorio añadido.
  - `mark_reminder_as_sent(reminder_id: int) -> None`:
    - **Descripción:** Marca un recordatorio como enviado.
    - **Entrada:** `reminder_id` (int): El ID del recordatorio.
  - `get_pending_reminders()`:
    - **Descripción:** Obtiene todos los recordatorios pendientes.
    - **Salida:** (list[Reminder]): La lista de recordatorios pendientes.

## Documentación de Esquemas en `app/schemas`

### [`event_reminder_schema.py`](./app/schemas/event_reminder_schema.py)
Este archivo define los esquemas relacionados con los recordatorios de eventos.

- **Clases:**
  - `EventReminderSchema`:
    - **Atributos:**
      - `index` (int): Índice del recordatorio.
      - `message` (str): Mensaje del recordatorio.
      - `reminder_time` (datetime): Fecha y hora del recordatorio.
  - `CreateEventRequest`:
    - **Atributos:**
      - `name` (str): Nombre del evento.
      - `description` (str): Descripción del evento.
      - `event_date` (datetime): Fecha del evento.
      - `reminders` (List[EventReminderSchema]): Lista de recordatorios asociados al evento.

### [`lead.py`](./app/schemas/lead.py)
Este archivo define el esquema para los datos de los leads.

- **Clases:**
  - `Lead`:
    - **Atributos:**
      - `first_name` (str): Nombre del lead.
      - `last_name` (str): Apellido del lead.
      - `email` (EmailStr): Correo electrónico del lead.
      - `country` (str): País del lead.
      - `phone` (str): Número de teléfono del lead.
      - `event_id` (int): ID del evento asociado.

### [`lead_reminder_response.py`](./app/schemas/lead_reminder_response.py)
Este archivo define el esquema para las respuestas de estado de recordatorios de leads.

- **Clases:**
  - `LeadReminderResponse`:
    - **Atributos:**
      - `first_name` (str): Nombre del lead.
      - `last_name` (str): Apellido del lead.
      - `email` (str): Correo electrónico del lead.
      - `country` (str): País del lead.
      - `phone` (str): Número de teléfono del lead.
      - `event_name` (str): Nombre del evento asociado.
      - `event_date` (datetime): Fecha del evento asociado.
      - `reminder_1_status` (Optional[bool]): Estado del primer recordatorio.
      - `reminder_2_status` (Optional[bool]): Estado del segundo recordatorio.
      - `reminder_3_status` (Optional[bool]): Estado del tercer recordatorio.

### [`lead_response.py`](./app/schemas/lead_response.py)
Este archivo define el esquema para las respuestas de leads.

- **Clases:**
  - `LeadResponse`:
    - **Atributos:**
      - `first_name` (str): Nombre del lead.
      - `last_name` (str): Apellido del lead.
      - `email` (str): Correo electrónico del lead.
      - `country` (str): País del lead.
      - `phone` (str): Número de teléfono del lead.
      - `event_name` (str): Nombre del evento asociado.
      - `registered_at` (Optional[datetime]): Fecha de registro del lead.

### [`message.py`](./app/schemas/message.py)
Este archivo define el esquema para los mensajes.

- **Clases:**
  - `MessageSchema`:
    - **Atributos:**
      - `id` (int): Identificador único del mensaje.
      - `recipient` (str): Destinatario del mensaje.
      - `content` (str): Contenido del mensaje.
      - `sent_at` (datetime): Fecha y hora de envío del mensaje.
      - `is_successful` (bool): Indica si el mensaje fue enviado exitosamente.
      - `error_message` (str): Mensaje de error si el envío falló.

## Documentación de Servicios en `app/services`

### [`lead_service.py`](./app/services/lead_service.py)
Este archivo gestiona las operaciones relacionadas con los leads y sus eventos.

- **Funciones:**
  - `register_lead(lead_data: LeadSchema) -> Lead`:
    - **Descripción:** Registra un nuevo lead, envía un mensaje de bienvenida y programa los recordatorios del evento asociado.
    - **Entrada:** `lead_data` (LeadSchema): Los datos del lead a registrar.
    - **Salida:** (Lead): El lead registrado.
  - `get_all_leads_with_events() -> List[LeadResponse]`:
    - **Descripción:** Obtiene todos los leads con sus eventos asociados.
    - **Salida:** (List[LeadResponse]): La lista de leads con eventos.
  - `get_leads_by_event(event_id: int) -> List[LeadResponse]`:
    - **Descripción:** Obtiene todos los leads asociados a un evento específico.
    - **Entrada:** `event_id` (int): El ID del evento.
    - **Salida:** (List[LeadResponse]): La lista de leads asociados al evento.
  - `get_lead_reminder_statuses() -> List[LeadReminderResponse]`:
    - **Descripción:** Obtiene el estado de los recordatorios de los leads.
    - **Salida:** (List[LeadReminderResponse]): La lista de estados de recordatorios.

### [`message_service.py`](./app/services/message_service.py)
Este archivo gestiona las operaciones relacionadas con los mensajes.

- **Funciones:**
  - `get_all_messages()`:
    - **Descripción:** Obtiene todos los mensajes.
    - **Salida:** (List[MessageSchema]): La lista de mensajes.
  - `get_message_by_id(message_id: int)`:
    - **Descripción:** Obtiene un mensaje por su ID.
    - **Entrada:** `message_id` (int): El ID del mensaje.
    - **Salida:** (MessageSchema): El mensaje correspondiente al ID.

### [`scheduler_service.py`](./app/services/scheduler_service.py)
Este archivo gestiona la programación de recordatorios utilizando APScheduler.

- **Funciones:**
  - `start()`:
    - **Descripción:** Inicia el programador de tareas si no está ya en ejecución.
  - `schedule_reminders(lead_name: str, lead_phone: str, lead_event_id: int, event_reminders: list[EventReminder])`:
    - **Descripción:** Programa los recordatorios de un evento para un lead específico.
    - **Entrada:** 
      - `lead_name` (str): Nombre del lead.
      - `lead_phone` (str): Teléfono del lead.
      - `lead_event_id` (int): ID de la relación lead-event.
      - `event_reminders` (list[EventReminder]): Lista de recordatorios del evento.
  - `send_reminder(lead_phone: str, message: str, reminder_id: int)`:
    - **Descripción:** Envía un recordatorio y marca el recordatorio como enviado en la base de datos.
    - **Entrada:** 
      - `lead_phone` (str): Teléfono del lead.
      - `message` (str): Mensaje del recordatorio.
      - `reminder_id` (int): ID del recordatorio.
  - `load_pending_reminders()`:
    - **Descripción:** Carga y programa todos los recordatorios pendientes.

### [`twilio_service.py`](./app/services/twilio_service.py)
Este archivo gestiona el envío de mensajes utilizando la API de Twilio.

- **Funciones:**
  - `send_message(number: str, message: str)`:
    - **Descripción:** Envía un mensaje a través de Twilio.
    - **Entrada:** 
      - `number` (str): Número de teléfono del destinatario.
      - `message` (str): Contenido del mensaje.
    - **Salida:** (str): El SID del mensaje enviado si es exitoso.
    - **Excepciones:** Lanza una `HTTPException` si el envío del mensaje falla.

## Documentación de Templates en `app/templates`

### [`messages_templates.py`](./app/templates/messages_templates.py)
Este archivo contiene funciones para generar plantillas de mensajes utilizados en la aplicación.

- **Funciones:**
  - `get_welcome_message(name: str, date: str, hour: str) -> str`:
    - **Descripción:** Genera un mensaje de bienvenida personalizado.
    - **Entrada:**
      - `name` (str): Nombre del destinatario.
      - `date` (str): Fecha del evento.
      - `hour` (str): Hora del evento.
    - **Salida:** (str): Mensaje de bienvenida formateado.

  - `get_24_hour_reminder(event_time: str, zoom_url: str) -> str`:
    - **Descripción:** Genera un recordatorio para 24 horas antes del evento.
    - **Entrada:**
      - `event_time` (str): Hora del evento.
      - `zoom_url` (str): Enlace de Zoom para el evento.
    - **Salida:** (str): Mensaje de recordatorio para 24 horas antes del evento.

  - `get_12_hour_reminder(event_time: str, zoom_url: str) -> str`:
    - **Descripción:** Genera un recordatorio para 12 horas antes del evento.
    - **Entrada:**
      - `event_time` (str): Hora del evento.
      - `zoom_url` (str): Enlace de Zoom para el evento.
    - **Salida:** (str): Mensaje de recordatorio para 12 horas antes del evento.

  - `get_beginning_reminder(zoom_url: str) -> str`:
    - **Descripción:** Genera un recordatorio para el inicio del evento.
    - **Entrada:** `zoom_url` (str): Enlace de Zoom para el evento.
    - **Salida:** (str): Mensaje de recordatorio para el inicio del evento.

## Documentación de `main.py`

### [`main.py`](./app/main.py)
Este archivo es el punto de entrada principal de la aplicación FastAPI.

- **Descripción:**
  - Configura la aplicación FastAPI.
  - Incluye la configuración de middleware y el enrutador principal.
  - Define eventos de inicio para la creación de tablas en la base de datos.

- **Componentes:**
  - `FastAPI`:
    - **Descripción:** Inicializa la aplicación FastAPI con un título y una versión obtenidos de la configuración.
  - `api_router`:
    - **Descripción:** Incluye el enrutador principal que agrupa las rutas definidas en la aplicación.
  - `CORSMiddleware`:
    - **Descripción:** Añade soporte para Cross-Origin Resource Sharing (CORS), permitiendo que la aplicación acepte solicitudes de cualquier origen.
    - **Parámetros:**
      - `allow_origins` (list): Lista de orígenes permitidos. En este caso, permite solicitudes de cualquier origen (`"*"`).
      - `allow_credentials` (bool): Permite el envío de credenciales.
      - `allow_methods` (list): Lista de métodos HTTP permitidos. En este caso, permite todos los métodos (`"*"`).
      - `allow_headers` (list): Lista de encabezados permitidos. En este caso, permite todos los encabezados (`"*"`).

- **Eventos:**
  - `startup_event`:
    - **Descripción:** Evento que se ejecuta al iniciar la aplicación, creando las tablas en la base de datos si no existen.