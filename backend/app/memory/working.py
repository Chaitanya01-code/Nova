from typing import List

from app.memory.memory_types import MemoryRecord


class WorkingMemory:
    """Working memory for the current operation context."""

    def __init__(self):
        self.records: List[MemoryRecord] = []

    def push(self, content: str, metadata: dict | None = None) -> MemoryRecord:
        record = MemoryRecord(
            memory_id=f"working-{len(self.records) + 1}",
            memory_type="working",
            content=content,
            metadata=metadata or {},
        )
        self.records.append(record)
        return record
