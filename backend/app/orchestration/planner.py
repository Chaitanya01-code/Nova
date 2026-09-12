from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class WorkflowTask:
    name: str
    agent: str
    tool: str = ""
    payload: Dict[str, Any] = field(default_factory=dict)


class WorkflowPlanner:
    """Create a deterministic multi-agent workflow from a request context."""

    def build(self, transcript: str, intent: str = "respond") -> List[WorkflowTask]:
        tasks = []
        lowered = (transcript or "").lower()

        # If the user means "open" then map the request into a desktop launch + browser open
        # that Nova can execute in a real workflow.
        if intent == "open" or any(word in lowered for word in ["open", "launch", "start"]):
            app = "notepad" if "notepad" in lowered else "calc"
            url = "https://example.com"

            tasks.append(
                WorkflowTask(
                    name="understand",
                    agent="general",
                    tool="launch_app",
                    payload={"app": app, "transcript": transcript},
                )
            )
            tasks.append(
                WorkflowTask(
                    name="browse",
                    agent="general",
                    tool="browser_open",
                    payload={"url": url, "transcript": transcript},
                )
            )
            tasks.append(
                WorkflowTask(
                    name="respond",
                    agent="general",
                    tool="notifications",
                    payload={"message": f"Opening desktop app {app} and browser page {url}"},
                )
            )
            return tasks

        agent = "general"
        if intent == "create":
            agent = "coding"
            tool = "write_file"
        elif intent == "repair":
            agent = "debugging"
            tool = "execute_terminal"
        elif intent == "plan":
            agent = "planning"
            tool = "write_file"
        else:
            agent = "general"
            tool = "web_fetch"

        tasks.append(WorkflowTask(name="understand", agent=agent, tool=tool, payload={"transcript": transcript}))
        tasks.append(WorkflowTask(name="respond", agent="general", tool="notifications", payload={"message": transcript[:80]}))
        return tasks
