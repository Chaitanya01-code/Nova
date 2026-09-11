from typing import Dict, Iterable, List, Optional

from app.tools.base import BaseTool


class ToolRegistry:
    """In-memory registry that maps Nova tool names to tool instances."""

    def __init__(self):
        self._tools: Dict[str, BaseTool] = {}

    def register(self, tool: BaseTool) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> Optional[BaseTool]:
        return self._tools.get(name)

    def list(self) -> List[str]:
        return sorted(self._tools.keys())

    def all(self) -> Iterable[BaseTool]:
        return self._tools.values()
