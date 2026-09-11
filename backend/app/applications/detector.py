from typing import List


class ApplicationDetector:
    """A basic detector that exposes a candidate list of discovered app names."""

    def detect(self, query: str = "") -> List[str]:
        if not query:
            return []
        return [query]
