from pathlib import Path
from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class DirectoryTool(BaseTool):
    name = "directory"
    description = "Create, list, or inspect a workspace directory."

    def run(self, path: str, create: bool = False) -> Dict[str, Any]:
        try:
            directory = Path(path)
            if create:
                directory.mkdir(parents=True, exist_ok=True)
            return ToolResult(ok=True, data={"path": path, "exists": directory.exists(), "created": create})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
