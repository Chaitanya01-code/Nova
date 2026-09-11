from pathlib import Path
from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class ReadFileTool(BaseTool):
    name = "read_file"
    description = "Read a file from the workspace filesystem."

    def run(self, path: str, encoding: str = "utf-8") -> Dict[str, Any]:
        try:
            content = Path(path).read_text(encoding=encoding)
            return ToolResult(ok=True, data={"path": path, "content": content})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
