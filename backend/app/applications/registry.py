from typing import Dict, Iterable, List, Optional

from app.applications.application import Application


class ApplicationRegistry:
    """Store external applications that Nova can discover or connect to."""

    def __init__(self):
        self._apps: Dict[str, Application] = {}

    def register(self, app: Application) -> None:
        self._apps[app.name] = app

    def get(self, name: str) -> Optional[Application]:
        return self._apps.get(name)

    def list(self) -> List[str]:
        return sorted(self._apps.keys())

    def all(self) -> Iterable[Application]:
        return self._apps.values()
