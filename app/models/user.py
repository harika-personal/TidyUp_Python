# USER (5 fields)
# ├── id, name, email, password, created_at, status, deactivated_at
# └── Relations:
#     ├── houses (via Housemates)
#     ├── houses_created
#     ├── chores_created
#     └── assignments


from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class User(Base):
    __tablename__ = "users"

    # Columns
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)  # Will store hashed password
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String, nullable=False, default="active")
    deactivated_at = Column(DateTime(timezone=True), nullable=True)


    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"