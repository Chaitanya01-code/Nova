import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from app.memory.memory_types import MemoryRecord, MemoryStore


class JsonMemoryStorage:
    """Simple file-backed storage for Nova memory records."""

    def __init__(self, path: str = "memory.json"):
        self.path = Path(path)
        self.store = MemoryStore()
        if self.path.exists():
            self._load()

    def add(self, record: MemoryRecord) -> None:
        self.store.add(record)
        self._save()

    def list(self, memory_type: Optional[str] = None) -> List[MemoryRecord]:
        return self.store.list(memory_type)

    def _save(self) -> None:
        payload = [r.__dict__ for r in self.store.records]
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def _load(self) -> None:
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except Exception:
            return

        for item in data:
            self.store.add(MemoryRecord(**item))
