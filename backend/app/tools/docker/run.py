from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class DockerRunTool(BaseTool):
    name = "docker_run"
    description = "Create a docker run command description object."

    def run(self, image: str, command: str = "") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"image": image, "command": command, "status": "run_request_created"})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
