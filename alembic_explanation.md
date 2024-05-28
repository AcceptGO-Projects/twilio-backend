# Explicación del Código en la Carpeta `alembic`

## Documentación de Archivos en `alembic`

### [`env.py`](./alembic/env.py)
Este archivo configura y ejecuta las migraciones de la base de datos utilizando Alembic.

- **Descripción:**
  - Configura el entorno para ejecutar migraciones en modos offline y online.
  - Utiliza la configuración de Alembic para obtener la URL de la base de datos y otros parámetros necesarios.

- **Componentes:**
  - `config`:
    - **Descripción:** Objeto de configuración de Alembic que proporciona acceso a los valores dentro del archivo `.ini` en uso.
  - `fileConfig(config.config_file_name)`:
    - **Descripción:** Configura los registradores de Python para la configuración de registro definida en el archivo de configuración de Alembic.
  - `target_metadata`:
    - **Descripción:** Metadata de los modelos de la base de datos, utilizada para soporte de autogeneración de migraciones.

- **Funciones:**
  - `run_migrations_offline()`:
    - **Descripción:** Ejecuta migraciones en modo "offline", configurando el contexto con solo una URL en lugar de un motor.
    - **Proceso:**
      - Configura el contexto con la URL de la base de datos.
      - Ejecuta las migraciones dentro de una transacción.
  - `run_migrations_online()`:
    - **Descripción:** Ejecuta migraciones en modo "online", creando un motor y asociando una conexión con el contexto.
    - **Proceso:**
      - Crea un motor a partir de la configuración.
      - Configura el contexto con la conexión y la metadata de destino.
      - Ejecuta las migraciones dentro de una transacción.

- **Modo de Ejecución:**
  - Determina si el contexto está en modo offline o online y ejecuta la función correspondiente (`run_migrations_offline` o `run_migrations_online`).

### [`script.py.mako`](./alembic/script.py.mako)
Este archivo es una plantilla Mako utilizada por Alembic para generar scripts de migración.

- **Descripción:**
  - Define la estructura y el contenido de los scripts de migración generados automáticamente.
  - Utiliza la sintaxis de Mako para insertar variables y lógica en el script de migración.

### [`alembic.ini`](./alembic.ini)
Este archivo es el archivo de configuración principal para Alembic.

- **Descripción:**
  - Contiene la configuración necesaria para ejecutar migraciones de base de datos utilizando Alembic.
  - Sirve para definir la ubicación de los scripts de migración, la URL de la base de datos y la configuración de registro.

- **Secciones Principales:**
  - `[alembic]`:
    - **Descripción:** Configuración general de Alembic.
    - **Parámetros:**
      - `script_location`: Ubicación de los scripts de Alembic.
      - `sqlalchemy.url`: URL de la base de datos utilizada para las migraciones.
  - `[logging]`:
    - **Descripción:** Configuración de registro para Alembic.
    - **Parámetros:**
      - `level`: Nivel de registro (e.g., `INFO`, `DEBUG`).
      - `file`: Archivo de registro si se especifica.
  - `[handlers]` y `[formatters]`:
    - **Descripción:** Configuración de los manejadores y formateadores de registros.
    - **Parámetros:**
      - `keys`: Claves que definen los manejadores y formateadores a utilizar.
  - `[logger]`:
    - **Descripción:** Configuración específica para los registradores.
    - **Parámetros:**
      - `level`: Nivel de registro.
      - `handlers`: Manejadores de registro a utilizar.

#### Ejemplo de Configuración:

```ini
[alembic]
script_location = alembic
sqlalchemy.url = sqlite:///example.db

[logging]
level = INFO
file = alembic.log

[handlers]
keys = fileHandler

[formatters]
keys = generic

[logger_root]
level = INFO
handlers = fileHandler
```