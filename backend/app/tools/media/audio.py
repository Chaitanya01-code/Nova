from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class MediaAudioTool(BaseTool):
    name = "media_audio"
    description = "Create a lightweight audio asset processing request object."

    def run(self, path: str, operation: str = "transcribe") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"path": path, "operation": operation, "status": "audio_request_created"})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
