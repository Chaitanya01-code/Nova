from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class EvaluationResult:
    passed: bool
    score: float
    feedback: str


class Evaluator:
    """Scores a proposed execution result for acceptance or retry."""

    def evaluate(self, result: Dict[str, Any]) -> EvaluationResult:
        status = str(result.get("status") or "unknown")
        if status == "success":
            return EvaluationResult(passed=True, score=1.0, feedback="Execution succeeded")
        return EvaluationResult(passed=False, score=0.0, feedback="Execution failed or was incomplete")
