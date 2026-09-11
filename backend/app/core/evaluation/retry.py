from typing import Dict, Any


class RetryPolicy:
    """Basic retry policy for a failed or low-confidence evaluation."""

    def __init__(self, max_attempts: int = 3):
        self.max_attempts = max_attempts

    def should_retry(self, evaluation: Dict[str, Any], attempts: int) -> bool:
        if attempts >= self.max_attempts:
            return False
        return bool(evaluation.get("passed") is False)
