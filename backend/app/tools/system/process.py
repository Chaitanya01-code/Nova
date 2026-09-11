from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class ProcessTool(BaseTool):
    name = "process"
    description = "Create a process status object for the current process environment."

    def run(self, pid: int = 0) -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"pid": pid, "status": "running"})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
