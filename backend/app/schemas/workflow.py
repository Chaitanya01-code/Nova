from typing import List, Dict, Any
from pydantic import BaseModel


class WorkflowTaskSchema(BaseModel):
    name: str
    agent: str
    tool: str = ""
    payload: Dict[str, Any] = {}


class WorkflowSchema(BaseModel):
    status: str = "ok"
    intent: str = "respond"
    transcript: str = ""
    workflow: List[WorkflowTaskSchema] = []
    return_context: Dict[str, Any] = {}
