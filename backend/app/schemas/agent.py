from typing import List, Dict, Any
from pydantic import BaseModel


class AgentSchema(BaseModel):
    name: str
    role: str
    metadata: Dict[str, Any] = {}


class AgentRunRequest(BaseModel):
    task: str
    context: str = ""


class AgentRunResponse(BaseModel):
    ok: bool
    agent: str
    content: str
    metadata: Dict[str, Any] = {}
    errors: List[str] = []
