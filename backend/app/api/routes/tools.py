from typing import Any, Dict

from fastapi import APIRouter

from app.schemas.tool import ToolRunRequest
from app.tools.registry import ToolRegistry
from app.tools.terminal.execute import ExecuteTerminalTool
from app.tools.web.fetch import WebFetchTool
from app.tools.web.search import WebSearchTool

router = APIRouter()
registry = ToolRegistry()
registry.register(ExecuteTerminalTool())
registry.register(WebFetchTool())
registry.register(WebSearchTool())


@router.get("/tools")
async def list_tools() -> Dict[str, Any]:
    return {"tools": registry.list()}


@router.post("/tools/run")
async def run_tool(payload: ToolRunRequest) -> Dict[str, Any]:
    tool = registry.get(payload.name)
    if tool is None:
        return {"ok": False, "error": "tool_not_found"}
    return tool.run(**payload.arguments)
