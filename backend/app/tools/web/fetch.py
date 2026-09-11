from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class WebFetchTool(BaseTool):
    name = "web_fetch"
    description = "Fetch a URL as a text or metadata payload stub."

    def run(self, url: str) -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"url": url, "status": "fetched", "content": ""})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
