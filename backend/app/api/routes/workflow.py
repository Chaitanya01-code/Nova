from typing import Any, Dict

from fastapi import APIRouter

from app.orchestration.orchestrator import NovaOrchestrator
from app.schemas.workflow import WorkflowSchema

router = APIRouter()


@router.post("/workflow")
async def run_workflow(payload: WorkflowSchema) -> Dict[str, Any]:
    orchestrator = NovaOrchestrator()
    result = orchestrator.run(payload.dict())
    return {"ok": True, "result": result}
