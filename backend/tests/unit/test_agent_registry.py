import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.agents.base.base_agent import BaseAgent
from app.agents.base.agent_registry import AgentRegistry
from app.agents.coding.agent import CodingAgent
from app.agents.research.agent import ResearchAgent
from app.agents.testing.agent import TestingAgent


def test_agent_registry_registers_and_exposes_multiagent_agents():
    registry = AgentRegistry()
    registry.register(CodingAgent())
    registry.register(ResearchAgent())
    registry.register(TestingAgent())

    assert isinstance(registry.get("coding"), BaseAgent)
    assert isinstance(registry.get("research"), BaseAgent)
    assert isinstance(registry.get("testing"), BaseAgent)
    assert "coding" in registry.list()
