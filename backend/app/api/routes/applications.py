from typing import Any, Dict, Optional

from fastapi import APIRouter

from app.applications.application import Application
from app.applications.application_info import ApplicationInfo
from app.applications.registry import ApplicationRegistry
from app.schemas.application import ApplicationSchema

router = APIRouter()
registry = ApplicationRegistry()


def _build_demo_application() -> Application:
    info = ApplicationInfo(name="nova-app", kind="internal", version="1.0", description="")
    return Application(name="nova-app", app_id="nova-app", info=info, capabilities=[], permissions=[], metadata={})


@router.get("/applications")
async def list_applications() -> Dict[str, Any]:
    registry.register(_build_demo_application())
    return {"applications": registry.list()}


@router.post("/applications")
async def create_application(payload: ApplicationSchema) -> Dict[str, Any]:
    payload_info = payload.info
    app_info = None
    if payload_info:
        app_info = ApplicationInfo(
            name=payload_info.name,
            kind=payload_info.kind,
            version=payload_info.version,
            description=payload_info.description,
            url=payload_info.url,
            icon=payload_info.icon,
        )

    app = Application(
        name=payload.name,
        app_id=payload.app_id,
        info=app_info,
        capabilities=payload.capabilities,
        permissions=payload.permissions,
        metadata=payload.metadata,
    )
    registry.register(app)
    return {"ok": True, "application": app.to_dict()}
