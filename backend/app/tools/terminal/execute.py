import subprocess
from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class ExecuteTerminalTool(BaseTool):
    name = "execute_terminal"
    description = "Execute a shell command in the workspace terminal."

    def run(self, command: str, cwd: str = ".", shell: bool = True) -> Dict[str, Any]:
        try:
            proc = subprocess.run(
                command,
                cwd=cwd,
                shell=shell,
                capture_output=True,
                text=True,
                check=False,
            )
            return ToolResult(
                ok=proc.returncode == 0,
                data={"returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr},
                error=None if proc.returncode == 0 else proc.stderr,
            )
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
