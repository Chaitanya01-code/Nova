from typing import Dict, Any, Optional


class StateManager:
    """Track the multi-agent workflow lifecycle by conversation or session ID."""

    def __init__(self):
        self._states: Dict[str, Dict[str, Any]] = {}

    def set(self, key: str, state: Dict[str, Any]) -> Dict[str, Any]:
        self._states[key] = state
        return state

    def get(self, key: str) -> Optional[Dict[str, Any]]:
        return self._states.get(key)

    def update(self, key: str, partial: Dict[str, Any]) -> Dict[str, Any]:
        current = self._states.get(key, {})
        current.update(partial)
        self._states[key] = current
        return current
