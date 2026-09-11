import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.applications.application import Application
from app.applications.application_info import ApplicationInfo
from app.applications.registry import ApplicationRegistry
from app.applications.capabilities import Capability
from app.applications.discovery import ApplicationDiscovery


def test_application_contract_objects_can_be_created():
    info = ApplicationInfo(name="gmail", kind="email", version="1.0")
    app = Application(name="gmail", app_id="gmail", info=info)
    registry = ApplicationRegistry()
    registry.register(app)
    discovery = ApplicationDiscovery()

    assert registry.get("gmail").name == "gmail"
    assert isinstance(Capability("read_mail"), Capability)
    assert discovery.scan("gmail") == ["gmail"]
