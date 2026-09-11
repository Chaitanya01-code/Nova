from typing import Any, Dict

from app.tools.base import BaseTool, ToolResult


class PythonExecuteTool(BaseTool):
    name = "python_execute"
    description = "Execute a short Python command expression and return the structured result."

    def run(self, code: str) -> Dict[str, Any]:
        try:
            namespace = {"__builtins__": __builtins__}
            exec(code, namespace, namespace)
            return ToolResult(ok=True, data={"code": code, "executed": True})
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
