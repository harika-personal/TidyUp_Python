# ASSIGNMENT (6 fields) - JOIN TABLE
# ├── id, assigned_user_id, chore_id, status, assigned_at, completed_at
# └── Relations:
#     ├── user (User)
#     └── chore (Chore)
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func

from app.database import Base


class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    assigned_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    assigned_chore_id = Column(Integer, ForeignKey("chores.id"), nullable=False)
    status = Column(String, nullable=False, default="active")
    completed_at = Column(DateTime(timezone=True), nullable=True)
    assigned_at = Column(DateTime(timezone=True), server_default=func.now())