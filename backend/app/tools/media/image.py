from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class MediaImageTool(BaseTool):
    name = "media_image"
    description = "Create a lightweight image processing request object."

    def run(self, path: str, operation: str = "inspect") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"path": path, "operation": operation, "status": "image_request_created"})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
