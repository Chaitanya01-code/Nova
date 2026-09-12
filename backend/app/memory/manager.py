from typing import Dict, List, Optional, Any

from app.memory.memory_types import MemoryRecord, MemoryStore


class MemoryManager:
    """High-level manager for storing and retrieving Nova memory records."""

    def __init__(self, store: Optional[MemoryStore] = None):
        self.store = store or MemoryStore()

    def add(self, memory_type: str, content: str, user_id: Optional[str] = None,
            project_id: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> MemoryRecord:
        record = MemoryRecord(
            memory_id=f"mem-{len(self.store.records) + 1}",
            memory_type=memory_type,
            user_id=user_id,
            project_id=project_id,
            content=content,
            metadata=metadata or {},
            created_at="now",
            updated_at="now",
        )
        self.store.add(record)
        return record

    def list(self, memory_type: Optional[str] = None) -> List[MemoryRecord]:
        return self.store.list(memory_type)

    def get(self, memory_id: str) -> Optional[MemoryRecord]:
        return self.store.get(memory_id)

    def semantic_search(self, keyword: str) -> List[MemoryRecord]:
        keyword = keyword.lower()
        return [r for r in self.store.records if keyword in r.content.lower()]
