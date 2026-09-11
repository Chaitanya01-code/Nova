from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class WebScrapeTool(BaseTool):
    name = "web_scrape"
    description = "Scrape a URL page and return a content summary stub."

    def run(self, url: str) -> Dict[str, Any]:
        try:
            return ToolResult(ok=True, data={"url": url, "scraped": True, "content": ""})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
