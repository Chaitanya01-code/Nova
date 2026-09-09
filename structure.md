# Nova Project Structure

This document describes the current project layout. Generated and ignored directories such as `node_modules/`, `dist/`, `__pycache__/`, and `.git/` are omitted.

```text
Nova/
|-- .github/
|   `-- workflows/
|       |-- cd.yml
|       |-- ci.yml
|       |-- docker.yml
|       `-- security.yml
|-- backend/
|   |-- Dockerfile
|   |-- requirements.txt
|   |-- app/
|   |   |-- __init__.py
|   |   |-- config.py
|   |   |-- dependencies.py
|   |   |-- main.py
|   |   |-- agents/
|   |   |   |-- __init__.py
|   |   |   |-- base/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- agent_context.py
|   |   |   |   |-- agent_registry.py
|   |   |   |   |-- agent_result.py
|   |   |   |   `-- base_agent.py
|   |   |   |-- browser/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- agent.py
|   |   |   |   `-- prompts.py
|   |   |   |-- coding/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- agent.py
|   |   |   |   `-- prompts.py
|   |   |   |-- computer/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- agent.py
|   |   |   |   `-- prompts.py
|   |   |   |-- data/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- agent.py
|   |   |   |   `-- prompts.py
|   |   |   |-- devops/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- agent.py
|   |   |   |   `-- prompts.py
|   |   |   |-- documentation/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- agent.py
|   |   |   |   `-- prompts.py
|   |   |   |-- file/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- agent.py
|   |   |   |   `-- prompts.py
|   |   |   |-- ml/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- agent.py
|   |   |   |   `-- prompts.py
|   |   |   |-- research/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- agent.py
|   |   |   |   `-- prompts.py
|   |   |   |-- security/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- agent.py
|   |   |   |   `-- prompts.py
|   |   |   |-- testing/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- agent.py
|   |   |   |   `-- prompts.py
|   |   |-- api/
|   |   |   |-- __init__.py
|   |   |   |-- middleware/
|   |   |   |   `-- __init__.py
|   |   |   `-- routes/
|   |   |       |-- __init__.py
|   |   |       |-- agents.py
|   |   |       |-- applications.py
|   |   |       |-- auth.py
|   |   |       |-- browser.py
|   |   |       |-- chat.py
|   |   |       |-- files.py
|   |   |       |-- health.py
|   |   |       |-- integrations.py
|   |   |       |-- memory.py
|   |   |       |-- model_lab.py
|   |   |       |-- models.py
|   |   |       |-- rag.py
|   |   |       |-- settings.py
|   |   |       |-- tasks.py
|   |   |       |-- tools.py
|   |   |       |-- users.py
|   |   |       `-- voice.py
|   |   |-- applications/
|   |   |   |-- __init__.py
|   |   |   |-- controller.py
|   |   |   |-- detector.py
|   |   |   |-- launcher.py
|   |   |   |-- permissions.py
|   |   |   |-- registry.py
|   |   |   |-- adapters/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- base.py
|   |   |   |   |-- chrome.py
|   |   |   |   |-- custom.py
|   |   |   |   |-- discord.py
|   |   |   |   |-- docker.py
|   |   |   |   |-- explorer.py
|   |   |   |   |-- spotify.py
|   |   |   |   |-- terminal.py
|   |   |   |   `-- vscode.py
|   |   |   `-- connectors/
|   |   |       |-- __init__.py
|   |   |       |-- custom/
|   |   |       |   |-- __init__.py
|   |   |       |   |-- client.py
|   |   |       |   `-- operations.py
|   |   |       |-- discord/
|   |   |       |   |-- __init__.py
|   |   |       |   |-- client.py
|   |   |       |   `-- operations.py
|   |   |       |-- github/
|   |   |       |   |-- __init__.py
|   |   |       |   |-- auth.py
|   |   |       |   |-- client.py
|   |   |       |   `-- operations.py
|   |   |       |-- google/
|   |   |       |   |-- __init__.py
|   |   |       |   |-- auth.py
|   |   |       |   |-- client.py
|   |   |       |   `-- operations.py
|   |   |       |-- notion/
|   |   |       |   |-- __init__.py
|   |   |       |   |-- client.py
|   |   |       |   `-- operations.py
|   |   |       `-- slack/
|   |   |           |-- __init__.py
|   |   |           |-- client.py
|   |   |           `-- operations.py
|   |   |-- background/
|   |   |   |-- __init__.py
|   |   |   |-- queue.py
|   |   |   |-- scheduler.py
|   |   |   |-- events.py
|   |   |   |-- task_executor.py
|   |   |   |-- worker_manager.py
|   |   |   `-- workers/
|   |   |       |-- __init__.py
|   |   |       |-- coding_worker.py
|   |   |       |-- general_worker.py
|   |   |       |-- monitoring_worker.py
|   |   |       |-- research_worker.py
|   |   |       `-- training_worker.py
|   |   |-- core/
|   |   |   |-- __init__.py
|   |   |   |-- nova.py
|   |   |   |-- context/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- context_builder.py
|   |   |   |   |-- context_manager.py
|   |   |   |   `-- context_window.py
|   |   |   |-- decision/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- engine.py
|   |   |   |   `-- policies.py
|   |   |   |-- evaluation/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- evaluator.py
|   |   |   |   |-- retry.py
|   |   |   |   `-- verifier.py
|   |   |   |-- execution/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- action.py
|   |   |   |   |-- executor.py
|   |   |   |   `-- result.py
|   |   |   |-- planning/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- plan_validator.py
|   |   |   |   |-- planner.py
|   |   |   |   `-- task_graph.py
|   |   |   `-- reasoning/
|   |   |       |-- __init__.py
|   |   |       |-- engine.py
|   |   |       `-- strategies.py
|   |   |-- database/
|   |   |   |-- __init__.py
|   |   |   |-- connection.py
|   |   |   |-- migrations/
|   |   |   |   `-- __init__.py
|   |   |   |-- models/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- agent.py
|   |   |   |   |-- api_key.py
|   |   |   |   |-- application.py
|   |   |   |   |-- audit_log.py
|   |   |   |   |-- conversation.py
|   |   |   |   |-- memory.py
|   |   |   |   |-- message.py
|   |   |   |   |-- model.py
|   |   |   |   |-- task.py
|   |   |   |   |-- tool.py
|   |   |   |   `-- user.py
|   |   |   `-- repositories/
|   |   |       |-- __init__.py
|   |   |       |-- conversation_repository.py
|   |   |       |-- memory_repository.py
|   |   |       |-- model_repository.py
|   |   |       |-- task_repository.py
|   |   |       `-- user_repository.py
|   |   |-- memory/
|   |   |   |-- __init__.py
|   |   |   |-- consolidation.py
|   |   |   |-- conversation.py
|   |   |   |-- embeddings.py
|   |   |   |-- episodic.py
|   |   |   |-- manager.py
|   |   |   |-- project.py
|   |   |   |-- memory_types.py
|   |   |   |-- retrieval.py
|   |   |   |-- semantic.py
|   |   |   |-- storage.py
|   |   |   |-- user.py
|   |   |   `-- working.py
|   |   |-- model_lab/
|   |   |   |-- __init__.py
|   |   |   |-- datasets/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- loader.py
|   |   |   |   |-- manager.py
|   |   |   |   `-- versioning.py
|   |   |   |-- deployment/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- deployer.py
|   |   |   |   `-- endpoint.py
|   |   |   |-- evaluation/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- benchmarks.py
|   |   |   |   |-- evaluator.py
|   |   |   |   `-- metrics.py
|   |   |   |-- experiments/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- experiment.py
|   |   |   |   `-- tracker.py
|   |   |   |-- finetuning/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- lora.py
|   |   |   |   `-- trainer.py
|   |   |   |-- preprocessing/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- cleaner.py
|   |   |   |   |-- pipeline.py
|   |   |   |   `-- tokenizer.py
|   |   |   |-- registry/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- registry.py
|   |   |   |   `-- versions.py
|   |   |   `-- training/
|   |   |       |-- __init__.py
|   |   |       |-- config.py
|   |   |       |-- distributed.py
|   |   |       `-- trainer.py
|   |   |-- models/
|   |   |   |-- __init__.py
|   |   |   |-- inference/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- engine.py
|   |   |   |   |-- generation.py
|   |   |   |   `-- streaming.py
|   |   |   |-- local/
|   |   |   |   `-- __init__.py
|   |   |   |-- providers/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- anthropic.py
|   |   |   |   |-- google.py
|   |   |   |   |-- local.py
|   |   |   |   `-- openai.py
|   |   |   `-- router/
|   |   |       |-- __init__.py
|   |   |       |-- cost_tracker.py
|   |   |       |-- health_checker.py
|   |   |       |-- model_registry.py
|   |   |       |-- model_selector.py
|   |   |       |-- router.py
|   |   |       `-- routing_policy.py
|   |   |-- monitoring/
|   |   |   |-- __init__.py
|   |   |   |-- health.py
|   |   |   |-- logging.py
|   |   |   `-- metrics.py
|   |   |-- orchestration/
|   |   |   |-- __init__.py
|   |   |   |-- agent_communication.py
|   |   |   |-- orchestrator.py
|   |   |   |-- planner.py
|   |   |   |-- task_manager.py
|   |   |   `-- workflow_engine.py
|   |   |-- rag/
|   |   |   |-- __init__.py
|   |   |   |-- chunking.py
|   |   |   |-- document_loader.py
|   |   |   |-- embeddings.py
|   |   |   |-- hybrid_search.py
|   |   |   |-- ingestion.py
|   |   |   |-- metadata.py
|   |   |   |-- pipeline.py
|   |   |   |-- reranker.py
|   |   |   `-- retrieval.py
|   |   |   `-- vector_store.py
|   |   |-- schemas/
|   |   |   `-- __init__.py
|   |   |-- security/
|   |   |   |-- __init__.py
|   |   |   |-- approval.py
|   |   |   |-- audit.py
|   |   |   |-- authentication.py
|   |   |   |-- authorization.py
|   |   |   |-- permissions.py
|   |   |   |-- policies.py
|   |   |   |-- risk_engine.py
|   |   |   |-- sandbox.py
|   |   |   |-- secrets.py
|   |   |   `-- tool_guard.py
|   |   |-- speech/
|   |   |   |-- __init__.py
|   |   |   |-- audio.py
|   |   |   |-- pipeline.py
|   |   |   |-- stt/
|   |   |   |   |-- __init__.py
|   |   |   |   |-- processor.py
|   |   |   |   |-- service.py
|   |   |   |   `-- whisper.py
|   |   |   `-- tts/
|   |   |       |-- __init__.py
|   |   |       |-- engine.py
|   |   |       |-- processor.py
|   |   |       `-- service.py
|   |   `-- tools/
|   |       |-- __init__.py
|   |       |-- base.py
|   |       |-- registry.py
|   |       |-- browser/
|   |       |   |-- __init__.py
|   |       |   |-- click.py
|   |       |   |-- open.py
|   |       |   |-- read_page.py
|   |       |   |-- screenshot.py
|   |       |   |-- search.py
|   |       |   `-- tabs.py
|   |       |-- database/
|   |       |   |-- __init__.py
|   |       |   |-- query.py
|   |       |   `-- schema.py
|   |       |-- docker/
|   |       |   |-- __init__.py
|   |       |   |-- build.py
|   |       |   |-- compose.py
|   |       |   |-- run.py
|   |       |   `-- stop.py
|   |       |-- filesystem/
|   |       |   |-- __init__.py
|   |       |   |-- delete.py
|   |       |   |-- directory.py
|   |       |   |-- read.py
|   |       |   |-- search.py
|   |       |   `-- write.py
|   |       |-- git/
|   |       |   |-- __init__.py
|   |       |   |-- branch.py
|   |       |   |-- clone.py
|   |       |   |-- commit.py
|   |       |   |-- push.py
|   |       |   `-- status.py
|   |       |-- media/
|   |       |   |-- __init__.py
|   |       |   |-- audio.py
|   |       |   |-- image.py
|   |       |   `-- video.py
|   |       |-- python/
|   |       |   |-- __init__.py
|   |       |   `-- execute.py
|   |       |-- system/
|   |       |   |-- __init__.py
|   |       |   |-- notifications.py
|   |       |   |-- process.py
|   |       |   `-- system_info.py
|   |       |-- terminal/
|   |       |   |-- __init__.py
|   |       |   |-- execute.py
|   |       |   `-- shell.py
|   |       `-- web/
|   |           |-- __init__.py
|   |           |-- fetch.py
|   |           |-- scrape.py
|   |           `-- search.py
|   `-- tests/
|       |-- agents/
|       |   |-- test_browser.py
|       |   |-- test_coding.py
|       |   `-- test_research.py
|       |-- applications/
|       |   |-- test_chrome.py
|       |   |-- test_terminal.py
|       |   `-- test_vscode.py
|       |-- integration/
|       |   |-- test_agents.py
|       |   |-- test_chat.py
|       |   `-- test_tools.py
|       |-- tools/
|       |   |-- test_browser.py
|       |   |-- test_filesystem.py
|       |   `-- test_terminal.py
|       `-- unit/
|           |-- test_core.py
|           |-- test_memory.py
|           |-- test_router.py
|           `-- test_security.py
|-- data/
|   |-- datasets/
|   |-- documents/
|   |-- embeddings/
|   |-- models/
|   |-- temporary/
|   `-- uploads/
|-- docs/
|   |-- agents/
|   |-- api/
|   |-- architecture/
|   |   |-- agent-architecture.md
|   |   |-- application-integration.md
|   |   |-- memory-architecture.md
|   |   |-- model-routing.md
|   |   |-- nova-core.md
|   |   |-- security-architecture.md
|   |   |-- system-architecture.md
|   |   `-- tool-architecture.md
|   |-- deployment/
|   `-- development/
|-- frontend/
|   |-- index.html
|   |-- package.json
|   |-- package-lock.json
|   |-- vite.config.js
|   |-- public/
|   `-- src/
|       |-- App.jsx
|       |-- main.jsx
|       |-- assets/
|       |-- components/
|       |   |-- agents/
|       |   |-- applications/
|       |   |-- browser/
|       |   |-- chat/
|       |   |-- common/
|       |   |-- files/
|       |   |-- memory/
|       |   |-- models/
|       |   |-- settings/
|       |   |-- tasks/
|       |   `-- voice/
|       |-- context/
|       |-- hooks/
|       |-- layouts/
|       |-- pages/
|       |   |-- Agents.jsx
|       |   |-- Applications.jsx
|       |   |-- Chat.jsx
|       |   |-- Home.jsx
|       |   |-- Memory.jsx
|       |   |-- ModelLab.jsx
|       |   |-- Models.jsx
|       |   |-- Settings.jsx
|       |   `-- Tasks.jsx
|       |-- services/
|       |   |-- agents.js
|       |   |-- api.js
|       |   |-- applications.js
|       |   |-- chat.js
|       |   `-- tasks.js
|       |-- stores/
|       |-- types/
|       `-- utils/
|-- infrastructure/
|   |-- docker/
|   |-- kubernetes/
|   |   |-- backend/
|   |   |-- frontend/
|   |   |-- monitoring/
|   |   |-- namespace/
|   |   |-- postgres/
|   |   |-- redis/
|   |   `-- workers/
|   |-- monitoring/
|   |   |-- grafana/
|   |   `-- prometheus/
|   |-- nginx/
|   `-- terraform/
|-- scripts/
|   |-- backup.py
|   |-- dev.ps1
|   |-- dev.sh
|   |-- health_check.py
|   |-- setup.ps1
|   `-- setup.sh
|-- .env.example
|-- .gitignore
|-- docker-compose.yml
|-- Makefile
|-- package.json
|-- README.md
`-- structure.md
```
