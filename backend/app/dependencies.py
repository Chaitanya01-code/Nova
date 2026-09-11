from typing import Generator

from app.config import Settings, get_settings


def get_settings_dependency() -> Generator[Settings, None, None]:
    yield get_settings()
