from dataclasses import dataclass, field
from typing import Dict, Any, List


@dataclass
class ExecutionResult:
    status: str
    summary: str
    data: Dict[str, Any] = field(default_factory=dict)
    warnings: List[str] = field(default_factory=list)
