from typing import Dict, Iterable, List, Optional

from app.agents.base.base_agent import BaseAgent


class AgentRegistry:
    """In-memory registry storing Nova agents by their role or canonical name."""

    def __init__(self):
        self._agents: Dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        self._agents[agent.name] = agent

    def get(self, name: str) -> Optional[BaseAgent]:
        return self._agents.get(name)

    def list(self) -> List[str]:
        return sorted(self._agents.keys())

    def all(self) -> Iterable[BaseAgent]:
        return self._agents.values()
