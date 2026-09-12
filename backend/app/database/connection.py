from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import get_settings


class DatabaseConnection:
    """Factory wrapper that wires the configured DB URL into SQLAlchemy objects."""

    def __init__(self, url: str | None = None):
        self.url = url or get_settings().database_url
        self.engine = create_engine(self.url, future=True)
        self.Session = sessionmaker(bind=self.engine)

    def session(self):
        return self.Session()


def get_session():
    return DatabaseConnection().session()
    
