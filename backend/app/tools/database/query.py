from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class DatabaseQueryTool(BaseTool):
    name = "database_query"
    description = "Execute a simple database query expression string."

    def run(self, query: str, connection: str = "default") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"query": query, "connection": connection, "result": []})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
