from typing import Optional, List

from app.database.connection import get_session
from app.database.models.memory import MemoryDB


class MemoryRepository:
    """Repository abstraction for persisting Nova memory records in SQLAlchemy-backed storage."""

    def __init__(self, session=None):
        self.session = session or get_session()

    def add(self, record: MemoryDB) -> None:
        self.session.add(record)
        self.session.commit()

    def list(self, memory_type: Optional[str] = None) -> List[MemoryDB]:
        query = self.session.query(MemoryDB)
        if memory_type:
            query = query.filter(MemoryDB.memory_type == memory_type)
        return query.all()

    def get(self, memory_id: str) -> Optional[MemoryDB]:
        return self.session.query(MemoryDB).filter(MemoryDB.id == memory_id).first()
