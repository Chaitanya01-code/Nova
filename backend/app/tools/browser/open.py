import webbrowser
from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class BrowserOpenTool(BaseTool):
    name = "browser_open"
    description = "Open a URL in the configured browser context."

    def run(self, url: str) -> Dict[str, Any]:
        try:
            opened = webbrowser.open_new_tab(url)
            return ToolResult(ok=opened, data={"url": url, "opened": opened})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
