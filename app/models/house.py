# HOUSE (8 fields)
# ├── id, name, address, created_by_id
# ├── invite_code, status, deactivated_at, created_at
# └── Relations:
#     ├── created_by (User)
#     ├── members (Housemates)
#     └── chores



from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.database import Base


class House(Base):
    __tablename__ = "houses"

    # Columns
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    invite_code = Column(String, unique=True, nullable=False, default=lambda: str(uuid.uuid4())[:8])
    status = Column(String, nullable=False, default="active")
    deactivated_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships

    def __repr__(self):
        return f"<House(id={self.id}, name={self.name}, status={self.status})>"