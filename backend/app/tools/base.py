from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseTool(ABC):
    """Abstract interface for all Nova backend tools."""

    name: str = "base_tool"
    description: str = "Base tool contract"

    @abstractmethod
    def run(self, **kwargs: Any) -> Dict[str, Any]:
        """Execute the tool and return a structured result payload."""


class ToolResult(dict):
    """Simple wrapper for tool responses to keep output consistent across domains."""

    def __init__(self, ok: bool = True, data: Optional[Dict[str, Any]] = None, error: Optional[str] = None):
        super().__init__()
        self["ok"] = ok
        self["data"] = data or {}
        self["error"] = error
