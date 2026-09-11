from pathlib import Path
from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class DeleteFileTool(BaseTool):
    name = "delete_file"
    description = "Delete a file safely from the workspace filesystem."

    def run(self, path: str) -> Dict[str, Any]:
        try:
            target = Path(path)
            if target.exists():
                target.unlink()
            return ToolResult(ok=True, data={"path": path, "deleted": True})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
