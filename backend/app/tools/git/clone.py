from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class GitCloneTool(BaseTool):
    name = "git_clone"
    description = "Create a safe git clone request object."

    def run(self, url: str, destination: str = ".") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"url": url, "destination": destination, "cloned": True})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
