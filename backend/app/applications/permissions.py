from dataclasses import dataclass, field
from typing import Dict, List, Any


@dataclass
class ApplicationPermission:
    name: str
    scope: str = "read"
    granted: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {"name": self.name, "scope": self.scope, "granted": self.granted}


class PermissionManager:
    """Policy envelope for application permission management."""

    def __init__(self):
        self.permissions: List[ApplicationPermission] = []

    def grant(self, permission: ApplicationPermission) -> ApplicationPermission:
        permission.granted = True
        self.permissions.append(permission)
        return permission

    def revoke(self, name: str) -> None:
        self.permissions = [p for p in self.permissions if p.name != name]
