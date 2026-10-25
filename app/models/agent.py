
from sqlalchemy import Column, Integer, String, Text, DateTime, text
from app.db.database import Base


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model_name = Column(String(100), nullable=False)
    system_prompt = Column(Text, nullable=False)
    status = Column(
        String(20),
        nullable=False,
        server_default=text("'created'")
    )
    created_at = Column(
        DateTime(timezone=True),
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP")
    )
