from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class ApplicationInfoSchema(BaseModel):
    name: str
    kind: str
    version: str = "1.0"
    description: str = ""
    url: Optional[str] = None
    icon: Optional[str] = None


class ApplicationSchema(BaseModel):
    name: str
    app_id: str
    info: Optional[ApplicationInfoSchema] = None
    capabilities: List[str] = []
    permissions: List[str] = []
    metadata: Dict[str, Any] = {}
