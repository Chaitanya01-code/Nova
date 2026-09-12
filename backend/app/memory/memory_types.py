from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class MemoryRecord:
    """Canonical data object for a Nova memory record."""

    memory_id: str
    memory_type: str
    user_id: Optional[str] = None
    project_id: Optional[str] = None
    content: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


@dataclass
class MemoryStore:
    """Simple in-memory store for Nova memories."""

    records: List[MemoryRecord] = field(default_factory=list)

    def add(self, record: MemoryRecord) -> None:
        self.records.append(record)

    def list(self, memory_type: Optional[str] = None) -> List[MemoryRecord]:
        if memory_type:
            return [r for r in self.records if r.memory_type == memory_type]
        return list(self.records)

    def get(self, memory_id: str) -> Optional[MemoryRecord]:
        for record in self.records:
            if record.memory_id == memory_id:
                return record
        return None
