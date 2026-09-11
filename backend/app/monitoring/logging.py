import logging
from typing import Any, Dict, Optional


class NovaLogger:
    """Small service wrapper around the standard library logger."""

    def __init__(self, name: str = "nova"):
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s"))
            self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def info(self, message: str, **kwargs: Any) -> None:
        self.logger.info(message, extra=kwargs)

    def warning(self, message: str, **kwargs: Any) -> None:
        self.logger.warning(message, extra=kwargs)

    def error(self, message: str, **kwargs: Any) -> None:
        self.logger.error(message, extra=kwargs)


def get_logger(name: str = "nova") -> NovaLogger:
    return NovaLogger(name)
