from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class Capability:
    name: str
    description: str = ""
    scopes: List[str] = None

    def __post_init__(self):
        if self.scopes is None:
            self.scopes = []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "scopes": self.scopes,
        }
