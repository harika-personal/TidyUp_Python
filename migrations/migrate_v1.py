# migrate_v1.py
import sys
import os

# Add the project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from app.database import engine, Base
from app.models import House, User, Chore, Housemate, Assignment



def create_tables():
    print("Creating database tables...")

    try:
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully")

        print("\nCreated tables:")
        for table in Base.metadata.sorted_tables:
            print(f" - {table.name}")

    except Exception as e:
        print(f"Error creating tables: {e}")


if __name__ == "__main__":
    create_tables()