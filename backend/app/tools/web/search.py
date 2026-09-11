from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class WebSearchTool(BaseTool):
    name = "web_search"
    description = "Search the web for a query and return a placeholder result list."

    def run(self, query: str) -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"query": query, "results": []})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
