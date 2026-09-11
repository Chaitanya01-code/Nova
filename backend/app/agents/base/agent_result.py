from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class AgentResult:
    ok: bool
    agent: str
    content: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ok": self.ok,
            "agent": self.agent,
            "content": self.content,
            "metadata": self.metadata,
            "errors": self.errors,
        }
