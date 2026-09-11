from typing import Any, Dict

from fastapi import APIRouter

from app.agents.base.agent_registry import AgentRegistry
from app.agents.coding.agent import CodingAgent
from app.agents.research.agent import ResearchAgent
from app.agents.testing.agent import TestingAgent
from app.schemas.agent import AgentRunRequest, AgentRunResponse

router = APIRouter()
registry = AgentRegistry()
registry.register(CodingAgent())
registry.register(ResearchAgent())
registry.register(TestingAgent())


@router.get("/agents")
async def list_agents() -> Dict[str, Any]:
    return {"agents": registry.list()}


@router.post("/agents/run", response_model=AgentRunResponse)
async def run_agent(payload: AgentRunRequest) -> Dict[str, Any]:
    agent = registry.get("coding") or CodingAgent()
    return agent.run({"transcript": payload.task}, {"context": payload.context})
