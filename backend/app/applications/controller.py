from typing import Any, Dict, Optional


class ApplicationController:
    """Coordinate actions against an application instance."""

    def __init__(self, app_id: str):
        self.app_id = app_id

    def handle(self, action: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {
            "app_id": self.app_id,
            "action": action,
            "status": "accepted",
            "payload": payload or {},
        }
