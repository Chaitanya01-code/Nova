import requests
from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class BrowserReadPageTool(BaseTool):
    name = "browser_read_page"
    description = "Read the visible page text or page payload from a browser page."

    def run(self, page: str = "default") -> Dict[str, Any]:
        try:
            if page.startswith("http://") or page.startswith("https://"):
                response = requests.get(page, timeout=10)
                response.raise_for_status()
                content = response.text[:5000]
                return ToolResult(ok=True, data={"page": page, "content": content})

            return ToolResult(ok=True, data={"page": page, "content": ""})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
