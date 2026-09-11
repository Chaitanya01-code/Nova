from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class ApplicationSession:
    app_id: str
    session_id: str
    token: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "app_id": self.app_id,
            "session_id": self.session_id,
            "token": self.token,
            "metadata": self.metadata,
        }
