from typing import List, Dict, Any, Optional


class AgentSelector:
    """Select an agent family based on an intent or context target."""

    def select(self, intent: str, context: Optional[Dict[str, Any]] = None) -> List[str]:
        intent = (intent or "general").lower()
        if intent == "create":
            return ["coding", "documentation"]
        if intent == "repair":
            return ["debugging", "testing"]
        if intent == "plan":
            return ["planning", "documentation"]
        if intent == "search":
            return ["research", "web"]
        return ["general"]
