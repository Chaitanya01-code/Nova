from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class DockerBuildTool(BaseTool):
    name = "docker_build"
    description = "Trigger a docker build command through the workspace command interface."

    def run(self, image: str, dockerfile: str = "Dockerfile") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"image": image, "dockerfile": dockerfile, "status": "build_request_created"})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
