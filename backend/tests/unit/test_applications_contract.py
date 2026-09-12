import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.applications.application import Application
from app.applications.application_info import ApplicationInfo
from app.applications.registry import ApplicationRegistry
from app.applications.capabilities import Capability
from app.applications.discovery import ApplicationDiscovery
from app.applications.launcher import ApplicationLauncher
from app.tools.browser.open import BrowserOpenTool
from app.orchestration.orchestrator import NovaOrchestrator


def test_application_contract_objects_can_be_created():
    info = ApplicationInfo(name="gmail", kind="email", version="1.0")
    app = Application(name="gmail", app_id="gmail", info=info)
    registry = ApplicationRegistry()
    registry.register(app)
    discovery = ApplicationDiscovery()

    assert registry.get("gmail").name == "gmail"
    assert isinstance(Capability("read_mail"), Capability)
    assert discovery.scan("gmail") == ["gmail"]


def test_runtime_action_contracts_are_available_for_launcher_and_browser_open():
    launcher = ApplicationLauncher()
    launched = launcher.launch("notepad")
    assert launched["app"] == "notepad"
    assert launched["status"] == "launched"

    open_tool = BrowserOpenTool()
    page_result = open_tool.run("https://example.com")
    assert page_result["ok"] is True
    assert page_result["data"]["opened"] is True
    assert page_result["data"]["url"] == "https://example.com"


def test_desktop_installed_application_can_be_opened_by_executable_name():
    launcher = ApplicationLauncher()
    result = launcher.launch("notepad.exe")
    assert result["status"] == "launched"
    assert result["opened"] is True
    assert result["app"] == "notepad.exe"


def test_orchestrator_can_execute_a_real_desktop_open_workflow():
    orchestrator = NovaOrchestrator()
    result = orchestrator.run("Open notepad now", intent="open", context="")
    assert result["status"] == "ok"
    assert len(result["workflow"]) >= 2
    assert result["execution"]["status"] == "success"
    assert any(step.get("tool") == "launch_app" for step in result["execution"]["steps"])
    assert any(step.get("tool") == "browser_open" for step in result["execution"]["steps"])
    assert "notepad" in str(result["execution"]) or "notepad" in str(result["workflow"])
    assert result["return_context"]["summary"]
