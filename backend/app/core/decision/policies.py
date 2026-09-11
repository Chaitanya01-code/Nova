from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class DecisionPolicy:
    allow_auto_execute: bool = False
    require_confirmation: bool = True
    max_risk: float = 0.4
    preferred_mode: str = "safe"


class PolicyEngine:
    """Turn reasoning output and planning state into a safe execution decision."""

    def decide(self, reasoning: Dict[str, Any], plan: Dict[str, Any]) -> Dict[str, Any]:
        risks = reasoning.get("risks") or []
        confidence = float(reasoning.get("confidence") or 0.0)

        allow_auto_execute = confidence >= 0.75 and len(risks) == 0
        require_confirmation = not allow_auto_execute

        return {
            "decision": "approve" if allow_auto_execute else "needs_confirmation",
            "policy": {
                "allow_auto_execute": allow_auto_execute,
                "require_confirmation": require_confirmation,
                "max_risk": 0.4,
                "preferred_mode": "safe",
            },
        }
