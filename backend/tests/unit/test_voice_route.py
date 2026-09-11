import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.api.routes.voice import voice_router


def test_voice_route_exists_and_has_understand_endpoint():
    routes = {route.path: route.name for route in voice_router.routes}
    assert "/understand" in routes
