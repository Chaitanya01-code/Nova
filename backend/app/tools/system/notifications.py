from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class NotificationsTool(BaseTool):
    name = "notifications"
    description = "Create a notification payload object for the user interface."

    def run(self, message: str, channel: str = "system") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"message": message, "channel": channel, "notified": True})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
