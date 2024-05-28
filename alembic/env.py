import os
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from dotenv import load_dotenv

load_dotenv()

# Configurar URL de la base de datos desde la variable de entorno
DATABASE_URL = os.getenv('DATABASE_URL') or 'mysql+pymysql://root:root@localhost:3306/leads_db'
DATABASE_URL.replace('mysql+aiomysql','mysql+pymysql')

if not DATABASE_URL:
    raise ValueError("No DATABASE_URL set for Alembic migration")

config = context.config

# Interpretar el archivo de configuración de logging.
fileConfig(config.config_file_name) # type: ignore

# Importar modelos de la aplicación aquí.
from app.models.base import Base  

target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_engine(
        DATABASE_URL,
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
