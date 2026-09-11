from typing import List


class ApplicationDiscovery:
    """Lightweight discovery contract for external app connections."""

    def scan(self, query: str = "") -> List[str]:
        if not query:
            return []
        return [query]
