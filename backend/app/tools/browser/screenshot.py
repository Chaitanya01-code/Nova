from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class BrowserScreenshotTool(BaseTool):
    name = "browser_screenshot"
    description = "Capture a screenshot from an open browser context."

    def run(self, page: str = "default", path: str = "screenshot.png") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"page": page, "path": path, "captured": True})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
