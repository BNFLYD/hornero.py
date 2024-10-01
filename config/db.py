# Dependencias
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.tables import Base
from dotenv import load_dotenv
import os
import psycopg2

# Importar los modelos de la base de datos
from models.users import User #1
from models.posts import Post #2
from models.comments import Comment #3
from models.likes import Like #4
from models.reposts import Repost #5
from models.messages import Message #6
from models.message_requests import MessageRequest #7
from models.media import Media #8
from models.follows import Follow #9
from models.blocks import Block #10
from models.links import Link #11
from models.trends import Trend #12
from models.lists import List #13
from models.list_members import ListMember #14

# Cargar las variables de entorno
load_dotenv()
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')

# Cadena de conexión
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Crear el engine
try:
    engine = create_engine(DATABASE_URL)
except Exception as e:
    print("Error al conectar a la base de datos:", e)

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Funcion para crear la base de datos (en caso de que no exista)
def create_database():
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        dbname='postgres'
    )
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{POSTGRES_DB}'")
    if cur.fetchone() is None:
        cur.execute(f"CREATE DATABASE {POSTGRES_DB}")
        print(f"Base de datos {POSTGRES_DB} creada con éxito")
    else:
        print(f"La base de datos {POSTGRES_DB} ya existe")
    cur.close()
    conn.close()

# Funcion para crear las tablas
def create_tables():
    try:
        Base.metadata.create_all(engine)
        print("Tablas creadas con éxito")
    except Exception as e:
        print("Error al crear las tablas:", e)

# Funcion para llamar a crear la base de datos y las tablas
def create_diagram(): 
    create_database()
    create_tables()