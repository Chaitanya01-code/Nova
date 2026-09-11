from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class BaseAgent(ABC):
    """Abstract contract for a Nova multi-agent execution unit."""

    name: str = "base"
    role: str = "general"

    @abstractmethod
    def run(self, task: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute a task and return an execution envelope."""
