from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class SystemInfoTool(BaseTool):
    name = "system_info"
    description = "Give a safe system identity and runtime metadata payload."

    def run(self) -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"platform": "python", "runtime": "workspace"})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
