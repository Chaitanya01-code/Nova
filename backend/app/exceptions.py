class NovaError(Exception):
    """Base exception used by Nova backend orchestration and route layers."""

    def __init__(self, message: str = "Nova backend error"):
        super().__init__(message)
        self.message = message


class ConfigurationError(NovaError):
    """Raised when environment or runtime configuration is incomplete."""


class ValidationError(NovaError):
    """Raised when request or model validation fails."""
