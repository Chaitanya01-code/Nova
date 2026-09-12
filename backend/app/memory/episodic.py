from typing import List

from app.memory.memory_types import MemoryRecord


class EpisodicMemory:
    """Episodic memory layer for event and session ordering traces."""

    def __init__(self):
        self.records: List[MemoryRecord] = []

    def remember(self, content: str, metadata: dict | None = None) -> MemoryRecord:
        record = MemoryRecord(
            memory_id=f"episodic-{len(self.records) + 1}",
            memory_type="episodic",
            content=content,
            metadata=metadata or {},
        )
        self.records.append(record)
        return record
