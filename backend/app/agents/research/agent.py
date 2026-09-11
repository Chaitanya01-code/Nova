from typing import Any, Dict, Optional

from app.agents.base.base_agent import BaseAgent
from app.agents.base.agent_result import AgentResult


class ResearchAgent(BaseAgent):
    name = "research"
    role = "research"

    def run(self, task: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        transcript = str(task.get("transcript") or "")
        return AgentResult(
            ok=True,
            agent=self.name,
            content=f"Research agent accepted task: {transcript[:80]}",
            metadata={"task": task, "context": context or {}},
        ).to_dict()
