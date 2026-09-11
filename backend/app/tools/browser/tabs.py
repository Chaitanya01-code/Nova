from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class BrowserTabsTool(BaseTool):
    name = "browser_tabs"
    description = "Return a simple list of browser tabs or browser page handles."

    def run(self, page: str = "default") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"page": page, "tabs": []})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
