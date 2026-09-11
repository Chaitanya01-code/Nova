from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application-level configuration surface used by Nova backend packages."""

    app_name: str = "nova"
    app_version: str = "0.1.0"
    debug: bool = False
    database_url: str = "sqlite:///./nova.db"

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()
