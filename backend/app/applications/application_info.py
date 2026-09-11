from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class ApplicationInfo:
    name: str
    kind: str
    version: str = "1.0"
    description: str = ""
    url: Optional[str] = None
    icon: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "kind": self.kind,
            "version": self.version,
            "description": self.description,
            "url": self.url,
            "icon": self.icon,
        }
