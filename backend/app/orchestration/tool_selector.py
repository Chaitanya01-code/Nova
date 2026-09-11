from typing import Dict, Any


class ToolSelector:
    """Pick a default tool type from a requested action intent."""

    def select(self, intent: str) -> str:
        if intent == "create":
            return "write_file"
        if intent == "repair":
            return "execute_terminal"
        if intent == "search":
            return "web_search"
        return "notifications"
