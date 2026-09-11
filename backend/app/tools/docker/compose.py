from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class DockerComposeTool(BaseTool):
    name = "docker_compose"
    description = "Generate a simple docker compose execution request shape."

    def run(self, command: str, project: str = "nova") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"command": command, "project": project, "status": "compose_request_created"})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
