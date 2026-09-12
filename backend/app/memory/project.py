from typing import List

from app.memory.memory_types import MemoryRecord


class ProjectMemory:
    """Project-level memory for persistent repository and workspace awareness."""

    def __init__(self):
        self.records: List[MemoryRecord] = []

    def remember(self, project_id: str, content: str, metadata: dict | None = None) -> MemoryRecord:
        record = MemoryRecord(
            memory_id=f"project-{len(self.records) + 1}",
            memory_type="project",
            project_id=project_id,
            content=content,
            metadata=metadata or {},
        )
        self.records.append(record)
        return record
