from typing import List, Dict, Any

from app.applications.launcher import ApplicationLauncher
from app.tools.browser.open import BrowserOpenTool


class ExecutionManager:
    """Simple execution manager that records a workflow step result and can call the tools it describes."""

    def execute(self, steps: List[Dict[str, Any]]) -> Dict[str, Any]:
        launcher = ApplicationLauncher()
        browser_open = BrowserOpenTool()
        execution_steps = []

        for step in steps:
            step = step if isinstance(step, dict) else {}
            tool = step.get("tool") if isinstance(step, dict) else "none"
            payload = step.get("payload") if isinstance(step, dict) else {}
            if not isinstance(payload, dict):
                payload = {}

            step_out = {
                "name": step.get("task") if isinstance(step, dict) else str(step),
                "agent": step.get("agent") if isinstance(step, dict) else "general",
                "tool": tool,
                "executed": True,
                "result": {},
            }

            if tool == "launch_app":
                app_name = payload.get("app") or "notepad"
                step_out["result"] = launcher.launch(app_name, metadata=payload)
                if not step_out["result"].get("opened"):
                    step_out["executed"] = False

            elif tool == "browser_open":
                url = payload.get("url") or "https://example.com"
                result = browser_open.run(url)
                step_out["result"] = result
                step_out["executed"] = bool(result.get("ok"))

            elif tool == "notifications":
                step_out["result"] = {"message": payload.get("message") or "Notification sent"}

            else:
                step_out["result"] = {"message": f"No real execution for {tool}"}

            execution_steps.append(step_out)

        return {
            "status": "success",
            "steps": execution_steps,
        }
