from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class BrowserSearchTool(BaseTool):
    name = "browser_search"
    description = "Perform a simple browser page search action."

    def run(self, query: str, page: str = "default") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"query": query, "page": page, "results": []})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
