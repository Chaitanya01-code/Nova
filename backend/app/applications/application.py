from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Application:
    name: str
    app_id: str
    info: "ApplicationInfo" = None
    capabilities: List[Any] = field(default_factory=list)
    permissions: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "app_id": self.app_id,
            "info": self.info.to_dict() if self.info else None,
            "capabilities": [cap.to_dict() if hasattr(cap, "to_dict") else str(cap) for cap in self.capabilities],
            "permissions": self.permissions,
            "metadata": self.metadata,
        }
