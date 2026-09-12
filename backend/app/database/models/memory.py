from typing import Optional
from sqlalchemy import Column, String, Text, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class MemoryDB(Base):
    __tablename__ = "nova_memory"

    id = Column(String, primary_key=True)
    memory_type = Column(String, nullable=False)
    user_id = Column(String, nullable=True)
    project_id = Column(String, nullable=True)
    content = Column(Text, nullable=False)
    metadata = Column(JSON, default=dict)
    created_at = Column(String, nullable=True)
    updated_at = Column(String, nullable=True)
