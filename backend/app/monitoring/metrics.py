from typing import Dict, Any


class MetricsRegistry:
    """In-memory registry for backend lifecycle and request metrics."""

    def __init__(self):
        self.metrics: Dict[str, Any] = {
            "requests_total": 0,
            "errors_total": 0,
            "latency_ms": 0,
        }

    def record_request(self, duration_ms: float = 0.0) -> None:
        self.metrics["requests_total"] += 1
        self.metrics["latency_ms"] = duration_ms

    def record_error(self) -> None:
        self.metrics["errors_total"] += 1

    def snapshot(self) -> Dict[str, Any]:
        return dict(self.metrics)
