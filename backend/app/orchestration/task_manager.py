from typing import Dict, Any, List


class TaskManager:
    """A lightweight task lifecycle manager for the orchestrator."""

    def __init__(self):
        self.tasks: List[Dict[str, Any]] = []

    def add(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.tasks.append(task)
        return task

    def list(self) -> List[Dict[str, Any]]:
        return self.tasks
