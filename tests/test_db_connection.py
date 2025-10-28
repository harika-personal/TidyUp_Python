import sys
import os

# Add the parent directory to Python path so it can find 'app'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import text
from app.database import engine


def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            version = result.fetchone()
            print("Database connection successful! :)")
            print(f"PostgreSQL version: {version[0]}")
    except Exception as e:
        print("Database connection failed! :(")
        print(f"Error: {e}")

if __name__ == "__main__":
    test_connection()

