from typing import Dict, Any


class ContextManager:
    """Simple in-memory persistence for Nova context snapshots."""

    def __init__(self):
        self._store: Dict[str, Dict[str, Any]] = {}

    def save(self, conversation_id: str, context: Dict[str, Any]) -> Dict[str, Any]:
        self._store[conversation_id] = context
        return context

    def load(self, conversation_id: str) -> Dict[str, Any]:
        return self._store.get(conversation_id, {})

    def reset(self, conversation_id: str) -> None:
        self._store.pop(conversation_id, None)
