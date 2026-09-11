from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class ReasoningOutput:
    intent: str
    goal: str
    assumptions: List[str]
    risks: List[str]
    confidence: float


class ReasoningEngine:
    """Transforms a NovaContext into a reasoning plan with assumptions and risks."""

    def analyze(self, context: Dict[str, Any]) -> ReasoningOutput:
        transcript = str(context.get("transcript") or "")
        intent = str(context.get("user_intent") or "respond")
        goal = f"Understand and respond to: {transcript[:80]}"

        assumptions = [
            "The user wants actionable help from the transcript.",
            "The transcript contains enough information to identify a service target.",
        ]

        risks = []
        if not transcript:
            risks.append("No transcript was provided.")
        if intent == "unknown":
            risks.append("Intent detection was inconclusive.")

        return ReasoningOutput(
            intent=intent,
            goal=goal,
            assumptions=assumptions,
            risks=risks,
            confidence=0.82,
        )
