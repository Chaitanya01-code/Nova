from typing import Dict, Any


class AgentCommunication:
    """A simple message bus for inter-agent communication handoffs."""

    def __init__(self):
        self.messages: list[Dict[str, Any]] = []

    def send(self, sender: str, receiver: str, message: str) -> Dict[str, Any]:
        payload = {"sender": sender, "receiver": receiver, "message": message}
        self.messages.append(payload)
        return payload
