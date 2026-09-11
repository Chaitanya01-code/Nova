from typing import Dict, Any


def health_check() -> Dict[str, Any]:
    """Return a lightweight backend health payload for monitoring probes."""
    return {
        "status": "ok",
        "service": "nova-backend",
        "checks": {
            "api": "ok",
            "database": "unknown",
            "queue": "unknown",
        },
    }
