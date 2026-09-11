from pathlib import Path
from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class WriteFileTool(BaseTool):
    name = "write_file"
    description = "Write content to a file on the workspace filesystem."

    def run(self, path: str, content: str, encoding: str = "utf-8") -> Dict[str, Any]:
        try:
            file_path = Path(path)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content, encoding=encoding)
            return ToolResult(ok=True, data={"path": path, "bytes_written": len(content.encode(encoding))})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
