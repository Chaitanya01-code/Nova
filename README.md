# Nova

Nova is an AI backend platform for converting text or speech input into an executable workflow, dispatching multi-agent reasoning, and returning a structured context for downstream applications.

## Features

1. User input can be text or speech, received through the voice and speech route layer.
2. Transcript and context normalization through the Nova context builder.
3. Reasoning analysis using the reasoning engine.
4. Planning support through the planner and workflow engine.
5. Policy-aware decision routing through the decision engine.
6. Tool execution through the tool registry and runtime integrations.
7. Agent execution through the coding, research, testing, and workflow agent layers.
8. Application integration through the multi-application discovery and connector registry.
9. Evaluation and verification for result quality and safety checks.
10. Memory and response context updates for project continuity.
11. Monitoring support through health, logging, and metrics services.

## Workflow

1. Receive text or speech input from the user.
2. Convert the speech stream into transcript text when voice input is used.
3. Build the Nova context object from the transcript and context payload.
4. Route the context through the Nova core flow of reasoning, planning, policy, and decision.
5. Dispatch the selected agent and tool chain through orchestration.
6. Execute the chosen workflow step through the orchestrator and execution manager.
7. Evaluate and verify the execution output.
8. Update memory and return the final context, execution payload, and workflow summary.

## Backend API

The backend exposes API routers for the voice route, core reasoning route, tools route, agents route, applications route, workflow route, and health route.

## Getting Started

Install dependencies and start the backend API service:

```bash
pip install -r backend/requirements.txt
uvicorn app.main:app --reload
```

