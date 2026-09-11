from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class MediaVideoTool(BaseTool):
    name = "media_video"
    description = "Create a lightweight video processing request object."

    def run(self, path: str, operation: str = "inspect") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"path": path, "operation": operation, "status": "video_request_created"})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
