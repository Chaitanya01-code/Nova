from pathlib import Path
from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class SearchFileTool(BaseTool):
    name = "search_file"
    description = "Search the workspace filesystem for a matching filename or substring."

    def run(self, root: str, pattern: str) -> Dict[str, Any]:
        try:
            matches = []
            for file in Path(root).rglob("*"):
                if pattern.lower() in str(file).lower():
                    matches.append(str(file))
            return ToolResult(ok=True, data={"root": root, "pattern": pattern, "matches": matches})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
