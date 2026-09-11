from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class GitBranchTool(BaseTool):
    name = "git_branch"
    description = "Return a safe branch listing command description."

    def run(self) -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"branches": []})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
