from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class PlanStep:
    name: str
    kind: str
    details: str = ""


@dataclass
class Plan:
    steps: List[PlanStep] = field(default_factory=list)


class Planner:
    """Construct a simple ordered task plan from the recognized intent."""

    def create_plan(self, context: Dict[str, Any]) -> Plan:
        intent = str(context.get("user_intent") or "respond")
        target = context.get("target") or "general"

        steps = [
            PlanStep(name="Understand", kind="analysis", details=f"Interpret the user statement: {context.get('transcript')}")
        ]

        if intent == "create":
            steps.append(PlanStep(name="Create artifacts", kind="build", details=f"Create or update {target} artifacts"))
        elif intent == "repair":
            steps.append(PlanStep(name="Diagnose issue", kind="debug", details=f"Investigate and fix {target}"))
        elif intent == "plan":
            steps.append(PlanStep(name="Draft plan", kind="planning", details=f"Build a structured schedule for {target}"))
        else:
            steps.append(PlanStep(name="Respond", kind="response", details="Return a concise solution or explanation"))

        return Plan(steps=steps)
