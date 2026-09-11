from typing import Dict, Any
from pydantic import BaseModel


class ToolSchema(BaseModel):
    name: str
    description: str = ""
    metadata: Dict[str, Any] = {}


class ToolRunRequest(BaseModel):
    name: str
    arguments: Dict[str, Any] = {}
