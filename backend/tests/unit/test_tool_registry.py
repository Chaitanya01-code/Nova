import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.tools.base import BaseTool
from app.tools.registry import ToolRegistry
from app.tools.filesystem.read import ReadFileTool
from app.tools.filesystem.write import WriteFileTool
from app.tools.terminal.execute import ExecuteTerminalTool


def test_tool_registry_registers_and_exposes_core_tools():
    registry = ToolRegistry()
    registry.register(ReadFileTool())
    registry.register(WriteFileTool())
    registry.register(ExecuteTerminalTool())

    assert isinstance(registry.get("read_file"), BaseTool)
    assert isinstance(registry.get("write_file"), BaseTool)
    assert isinstance(registry.get("execute_terminal"), BaseTool)
    assert "read_file" in registry.list()
