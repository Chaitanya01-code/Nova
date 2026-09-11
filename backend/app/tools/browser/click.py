from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class BrowserClickTool(BaseTool):
    name = "browser_click"
    description = "Click an element by selector in a browser context."

    def run(self, selector: str, page: str = "default") -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"selector": selector, "page": page, "clicked": True})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
