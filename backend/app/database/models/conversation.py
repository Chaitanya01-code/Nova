from sqlalchemy import Column, String, Text, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ConversationDB(Base):
    __tablename__ = "nova_conversation"

    id = Column(String, primary_key=True)
    user_id = Column(String, nullable=True)
    transcript = Column(Text, nullable=False)
    response = Column(Text, nullable=True)
    metadata = Column(JSON, default=dict)
