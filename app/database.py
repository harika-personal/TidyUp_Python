from dotenv import load_dotenv
import  os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DEBUG = os.getenv("DEBUG", "False") == "True"

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SSLMODE = os.getenv("DB_SSLMODE")

# Create connection string
DB_CONNECTION_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode={DB_SSLMODE}&channel_binding=require"

# Create SQLAlchemy engine
engine = create_engine(DB_CONNECTION_URL, echo=DEBUG)

# Create SessionLocal Class for database sessions
SessionLocal = sessionmaker(auto_commit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get database session
def get_db():
    """
    Dependency function to get database session.
    Yields a database session and ensures it's closed after use.
    :return:
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
