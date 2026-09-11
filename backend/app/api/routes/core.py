from typing import Any, Dict

from fastapi import APIRouter

from app.core.nova import NovaCore
from app.schemas.workflow import WorkflowSchema

router = APIRouter()
nova_core = NovaCore()


@router.post("/core/understand")
async def understand(payload: WorkflowSchema) -> Dict[str, Any]:
    return nova_core.process(payload.transcript, payload.return_context.get("context", ""))
