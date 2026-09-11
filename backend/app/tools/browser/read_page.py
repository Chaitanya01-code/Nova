from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class BrowserReadPageTool(BaseTool):
    name = "browser_read_page"
    description = "Read the visible page text or page payload from a browser page."

    def run(self, page: str = "default") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"page": page, "content": ""})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
