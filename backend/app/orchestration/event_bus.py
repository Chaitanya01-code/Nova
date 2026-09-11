from typing import Dict, Any, List


class EventBus:
    """Process-wide event publisher/subscriber hook for orchestration signals."""

    def __init__(self):
        self.listeners: List[Any] = []

    def subscribe(self, listener: Any) -> None:
        self.listeners.append(listener)

    def publish(self, event: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        for listener in self.listeners:
            try:
                listener(event, payload)
            except Exception:
                pass
        return {"event": event, "payload": payload}
