# CHORE (9 fields)
# ├── id, house_id, created_by_id, title, description
# ├── people_required, interval_days, status, due_date, created_at
# └── Relations:
#     ├── house (House)
#     ├── created_by (User)
#     └── assignments
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Chore(Base):
    __tablename__ = "chores"

    id = Column(Integer, primary_key=True, index=True)
    house_id = Column(Integer, ForeignKey("houses.id"), nullable=False)
    created_by_id = Column(Integer, ForeignKey("users.id"),nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    people_required = Column(Integer, nullable=False, default=1)
    interval_days = Column(Integer, nullable=False)
    status = Column(String, nullable=False, default="active")
    due_date = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # # Relationships
    # created_by = relationship("User", foreign_keys=[created_by_id], back_populates="chores_created")
    # belongs_to = relationship("House", foreign_keys=[house_id], back_populates="chores")

