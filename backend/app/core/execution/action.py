from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class Action:
    type: str
    description: str
    target: Optional[str] = None
    payload: Dict[str, Any] = None

    def __post_init__(self):
        if self.payload is None:
            self.payload = {}
