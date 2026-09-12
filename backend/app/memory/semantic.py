from typing import List

from app.memory.memory_types import MemoryRecord


class SemanticMemory:
    """Semantic memory layer for concept and fact recall in Nova."""

    def __init__(self):
        self.records: List[MemoryRecord] = []

    def remember(self, content: str, metadata: dict | None = None) -> MemoryRecord:
        record = MemoryRecord(
            memory_id=f"semantic-{len(self.records) + 1}",
            memory_type="semantic",
            content=content,
            metadata=metadata or {},
        )
        self.records.append(record)
        return record
