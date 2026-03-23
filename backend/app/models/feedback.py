from sqlalchemy import Column, DateTime, Integer, String, Text, func

from app.core.database import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), nullable=False)
    email = email = Column(String(255), nullable=True, index=True)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

