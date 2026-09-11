from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class DockerStopTool(BaseTool):
    name = "docker_stop"
    description = "Create a docker stop command description object."

    def run(self, container: str) -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"container": container, "status": "stop_request_created"})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
