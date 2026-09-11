from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Decision:
    action: str
    reason: str
    approved: bool


class DecisionEngine:
    """Makes the final decision based on policy and context."""

    def choose(self, context: Dict[str, Any], reasoning: Dict[str, Any], policy: Dict[str, Any]) -> Decision:
        allow_auto_execute = bool(policy.get("policy", {}).get("allow_auto_execute", False))
        if allow_auto_execute:
            return Decision(action="execute", reason="Safe to continue automatically.", approved=True)
        return Decision(action="clarify", reason="Human confirmation is required.", approved=False)
