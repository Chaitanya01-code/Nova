from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class WorkflowStep:
    task: str
    agent: str
    tool: str
    payload: Dict[str, Any]


class WorkflowEngine:
    """Coordinate workflow execution across tasks and agent/tool routing."""

    def run(self, tasks: List[Dict[str, Any]]) -> List[WorkflowStep]:
        steps = []
        for task in tasks:
            steps.append(WorkflowStep(
                task=task.get("name", "task"),
                agent=task.get("agent", "general"),
                tool=task.get("tool", "none"),
                payload=task.get("payload") or {},
            ))
        return steps
