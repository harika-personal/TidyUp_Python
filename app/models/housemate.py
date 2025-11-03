# HOUSEMATES (6 fields) - JOIN TABLE
# ├── id, user_id, house_id, role, joined_at, left_at
# └── Relations:
#     ├── user (User)
#     └── house (House)

from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, DATETIME, DateTime, func


class Housemate(Base):
    __tablename__ = "housemates"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    house_id = Column(Integer, ForeignKey("houses.id"), nullable=False)
    role = Column(String, nullable=False, default="member")
    joined_at = Column(DateTime(timezone=True), server_default=func.now(),)
    left_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships


