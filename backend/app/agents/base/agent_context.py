from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AgentContext:
    transcript: str = ""
    intent: str = "respond"
    target: Optional[str] = None
    conversation_id: Optional[str] = None
    context: Dict[str, Any] = field(default_factory=dict)
    memory: List[str] = field(default_factory=list)
