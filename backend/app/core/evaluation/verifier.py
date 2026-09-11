from typing import Dict, Any


class Verifier:
    """Validate a result object and return readiness for final context."""

    def verify(self, result: Dict[str, Any]) -> bool:
        if not isinstance(result, dict):
            return False
        return bool(result.get("status") in {"success", "needs_confirmation", "partial"})
