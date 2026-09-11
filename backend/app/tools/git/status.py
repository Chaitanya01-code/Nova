from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class GitStatusTool(BaseTool):
    name = "git_status"
    description = "Return an empty git status result suitable for orchestration UI."

    def run(self) -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"branch": "main", "modified": [], "status": "clean"})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
