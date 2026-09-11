class ContextWindow:
    """Trims an accumulated transcript/context string to a safe length."""

    def __init__(self, max_chars: int = 4000):
        self.max_chars = max_chars

    def trim(self, text: str) -> str:
        if not text:
            return ""
        if len(text) <= self.max_chars:
            return text
        return text[: self.max_chars - 3] + "..."
