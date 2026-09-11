# Nova

Nova is an AI backend platform for converting user voice and text into an executable workflow, dispatching multi-agent reasoning, and returning a structured context for downstream applications.

## Features

1. Voice input support through the speech and voice route layer.
2. Transcript-to-context building through the Nova context builder.
3. Reasoning analysis using the reasoning engine.
4. Planning support through the planner and workflow engine.
5. Policy-aware decision routing through the decision engine.
6. Tool execution through the tool registry and runtime integrations.
7. Agent execution through the coding, research, testing, and workflow agent layers.
8. Application integration through the multi-application discovery and connector registry.
9. Evaluation and verification for result quality and safety checks.
10. Monitoring support through health, logging, and metrics services.

## Workflow

1. Receive the transcript or prompt from the user.
2. Build the Nova context object from that transcript.
3. Run the reasoning engine to analyze goals, assumptions, risks, and confidence.
4. Create an execution plan from the planner.
5. Apply policy and decision selection.
6. Dispatch the selected agent and tool chain.
7. Execute the chosen workflow step through the orchestrator and execution manager.
8. Evaluate the result and verify that the output is consistent.
9. Return the final context, execution payload, and workflow summary.

## Backend API

The backend exposes API routers for the voice route, core reasoning route, tools route, agents route, applications route, workflow route, and health route.

## Getting Started

Install dependencies and start the backend API service:

```bash
pip install -r backend/requirements.txt
uvicorn app.main:app --reload
```

