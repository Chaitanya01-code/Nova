from app.main import app


def test_expected_api_routes_registered():
    paths = sorted(route.path for route in app.routes if hasattr(route, "path"))
    assert "/api/voice/understand" in paths
    assert "/api/tools" in paths
    assert "/api/agents" in paths
    assert "/api/applications" in paths
    assert "/api/workflow" in paths
