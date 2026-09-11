from typing import List, Dict, Any


class ExecutionManager:
    """Simple execution manager that records a workflow step result."""

    def execute(self, steps: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            "status": "success",
            "steps": [
                {
                    "name": step.get("task") if isinstance(step, dict) else str(step),
                    "agent": step.get("agent") if isinstance(step, dict) else "general",
                    "tool": step.get("tool") if isinstance(step, dict) else "none",
                    "executed": True,
                }
                for step in steps
            ],
        }
