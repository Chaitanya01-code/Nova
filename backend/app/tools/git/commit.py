from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class GitCommitTool(BaseTool):
    name = "git_commit"
    description = "Create a git commit command description object."

    def run(self, message: str, add_all: bool = True) -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"message": message, "stage_all": add_all, "commit_created": True})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
