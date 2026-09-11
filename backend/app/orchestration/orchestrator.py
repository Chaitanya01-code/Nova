from typing import Dict, Any, List

from app.orchestration.agent_selector import AgentSelector
from app.orchestration.planner import WorkflowPlanner
from app.orchestration.workflow_engine import WorkflowEngine
from app.orchestration.execution_manager import ExecutionManager


class NovaOrchestrator:
    """Top-level multi-agent coordinator for Nova conversation and action workflows."""

    def __init__(self):
        self.agent_selector = AgentSelector()
        self.planner = WorkflowPlanner()
        self.workflow_engine = WorkflowEngine()
        self.execution_manager = ExecutionManager()

    def run(self, transcript: str, intent: str = "respond", context: str = "") -> Dict[str, Any]:
        selected_agents = self.agent_selector.select(intent, {"transcript": transcript, "context": context})
        tasks = self.planner.build(transcript, intent)
        workflow_steps = self.workflow_engine.run([task.__dict__ for task in tasks])
        outcome = self.execution_manager.execute([step.__dict__ for step in workflow_steps])

        return {
            "status": "ok",
            "agents": selected_agents,
            "intent": intent,
            "transcript": transcript,
            "workflow": [step.__dict__ for step in workflow_steps],
            "execution": outcome,
            "return_context": {
                "status": "ok",
                "summary": "The transcript was parsed into a workflow and dispatched through the Nova orchestration chain.",
                "agents": selected_agents,
            },
        }
