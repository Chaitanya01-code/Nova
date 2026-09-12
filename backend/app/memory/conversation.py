from typing import List

from app.memory.memory_types import MemoryRecord


class ConversationMemory:
    """Conversation memory for storing transcript and reply traces."""

    def __init__(self):
        self.records: List[MemoryRecord] = []

    def add_message(self, user_id: str, content: str, metadata: dict | None = None) -> MemoryRecord:
        record = MemoryRecord(
            memory_id=f"conversation-{len(self.records) + 1}",
            memory_type="conversation",
            user_id=user_id,
            content=content,
            metadata=metadata or {},
        )
        self.records.append(record)
        return record
