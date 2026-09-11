from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class GitPushTool(BaseTool):
    name = "git_push"
    description = "Create a git push request description object."

    def run(self, remote: str = "origin", branch: str = "main") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"remote": remote, "branch": branch, "pushed": True})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
