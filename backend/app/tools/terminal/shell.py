import subprocess
from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class ShellTool(BaseTool):
    name = "shell"
    description = "Open a shell command execution path for workspace commands."

    def run(self, command: str, cwd: str = ".") -> Dict[str, Any]:
        try:
            proc = subprocess.run(command, cwd=cwd, shell=True, capture_output=True, text=True)
            return ToolResult(
                ok=proc.returncode == 0,
                data={"returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr},
                error=None if proc.returncode == 0 else proc.stderr,
            )
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
