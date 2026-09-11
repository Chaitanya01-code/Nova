from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class DatabaseSchemaTool(BaseTool):
    name = "database_schema"
    description = "Return a synthetic schema description for a database context."

    def run(self, connection: str = "default") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"connection": connection, "tables": []})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
