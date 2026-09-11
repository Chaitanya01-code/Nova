from typing import Dict, Any, List


class TaskGraph:
    """A very simple dependency graph container for workflow tasks."""

    def __init__(self):
        self.nodes: List[Dict[str, Any]] = []

    def add(self, task: Dict[str, Any]) -> None:
        self.nodes.append(task)

    def list(self) -> List[Dict[str, Any]]:
        return self.nodes
