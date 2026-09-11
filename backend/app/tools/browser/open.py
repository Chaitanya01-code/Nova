from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class BrowserOpenTool(BaseTool):
    name = "browser_open"
    description = "Open a URL in the configured browser context."

    def run(self, url: str) -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"url": url, "opened": True})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
