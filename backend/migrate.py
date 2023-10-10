# flask-react-chat-login/backend/migrate.py

from alembic import context
from sqlalchemy import create_engine
from sqlalchemy.ext import context as sa_context
from sqlalchemy.orm import sessionmaker
from models.usuario import Usuario  # Importe seus modelos aqui
from app import db  # Importe sua instância db aqui

# Configure o banco de dados
DATABASE_URL = "mysql://rpz:aves123456@localhost/Login_Flask_DB"

# Crie uma instância do SQLAlchemy Engine
engine = create_engine(DATABASE_URL)

# Crie uma sessão do SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Configure o contexto do Alembic
context.configure(
    connection=engine,
    target_metadata=db.metadata,  # Use o metadata do seu aplicativo SQLAlchemy
    include_schemas=True,
)

def run_migrations_offline():
    context.configure(url=DATABASE_URL, target_metadata=db.metadata)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=db.metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
