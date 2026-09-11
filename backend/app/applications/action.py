from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ApplicationAction:
    name: str
    description: str = ""
    parameters: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters,
        }
