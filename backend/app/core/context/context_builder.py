from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class NovaContext:
    transcript: str
    context: str = ""
    user_intent: str = "unknown"
    target: Optional[str] = None
    topics: List[str] = field(default_factory=list)
    entities: List[str] = field(default_factory=list)
    metadata: Dict[str, object] = field(default_factory=dict)


class ContextBuilder:
    """Normalize a user transcript into a reusable context object for planning."""

    @staticmethod
    def build(transcript: str, context: str = "") -> NovaContext:
        cleaned = (transcript or "").strip()
        if not cleaned:
            raise ValueError("transcript must not be empty")

        intent = ContextBuilder.detect_intent(cleaned)
        entities = []
        topics = []

        if "schedule" in cleaned.lower() or "meeting" in cleaned.lower():
            topics.append("schedule")
        if "email" in cleaned.lower() or "message" in cleaned.lower():
            topics.append("communication")
        if "code" in cleaned.lower() or "build" in cleaned.lower():
            topics.append("software")

        return NovaContext(
            transcript=cleaned,
            context=context,
            user_intent=intent,
            target=ContextBuilder.detect_target(cleaned),
            topics=topics,
            entities=entities,
            metadata={"language": "en", "source": "voice"},
        )

    @staticmethod
    def detect_intent(text: str) -> str:
        lowered = text.lower()
        if any(word in lowered for word in ["create", "make", "build", "write"]):
            return "create"
        if any(word in lowered for word in ["fix", "debug", "issue", "error"]):
            return "repair"
        if any(word in lowered for word in ["summarize", "explain", "understand"]):
            return "understand"
        if any(word in lowered for word in ["schedule", "meeting", "plan"]):
            return "plan"
        return "respond"

    @staticmethod
    def detect_target(text: str) -> Optional[str]:
        lowered = text.lower()
        if "email" in lowered:
            return "email"
        if "code" in lowered:
            return "code"
        if "task" in lowered:
            return "task"
        return None
