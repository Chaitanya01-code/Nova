from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List


@dataclass
class Task:
    id: str
    name: str
    agent: str
    tool: str = ""
    payload: Dict[str, Any] = field(default_factory=dict)
    dependencies: List[str] = field(default_factory=list)
    status: str = "pending"
