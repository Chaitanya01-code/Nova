import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.orchestration.orchestrator import NovaOrchestrator
from app.orchestration.agent_selector import AgentSelector
from app.orchestration.planner import WorkflowPlanner
from app.orchestration.workflow_engine import WorkflowEngine
from app.orchestration.execution_manager import ExecutionManager


def test_orchestrator_contract_exports_expected_components():
    orchestrator = NovaOrchestrator()
    assert hasattr(orchestrator, "run")
    assert isinstance(AgentSelector(), AgentSelector)
    assert isinstance(WorkflowPlanner(), WorkflowPlanner)
    assert isinstance(WorkflowEngine(), WorkflowEngine)
    assert isinstance(ExecutionManager(), ExecutionManager)
