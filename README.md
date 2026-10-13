# newtool

Local AI / RAG + Safety Assistant integrated toolkit.

## Project goals

This repository is the starting point for a modular research and safety-assistant platform with three main capability areas:

1. **Local AI** — local model providers, routing, prompts, and model-health checks.
2. **RAG** — document ingestion, retrieval, evidence/citation handling, and knowledge-base interfaces.
3. **Safety Assistant** — Windows/Android guardian-mode components, anomaly-event handling, local-first storage, and explicit emergency-action gates.

The first version intentionally focuses on a clean, testable skeleton. Production model inference, knowledge indexing, mobile clients, and emergency notification actions are **not implemented yet**.

## Repository layout

```text
newtool/
├── src/newtool/
│   ├── cli.py
│   ├── config.py
│   └── modules/
│       ├── local_ai/
│       ├── rag/
│       └── safety/
├── tests/
├── docs/
├── config.example.yaml
├── pyproject.toml
└── .gitignore
```

## Recommended implementation order

1. Configuration and health checks.
2. Local AI provider abstraction (Ollama first; optional cloud providers behind explicit configuration).
3. RAG retrieval interface and evidence model.
4. Document ingestion and staging, keeping production knowledge writes explicit.
5. Safety-assistant event model and local state.
6. Windows/Android communication layer.
7. Anomaly detection and confirmation countdown.
8. Notification integrations, only after explicit configuration and safety tests.
9. Long-term run history, learning records, evaluation, and controlled self-improvement.

## Adjustable parts

- Local model/provider and inference endpoint.
- Embedding model and vector database.
- Retrieval/reranking strategy.
- Data-retention location and duration.
- Safety thresholds and confirmation timeout.
- Notification providers.
- Cloud usage and privacy boundaries.

## Development principles

- Local-first for private data.
- Cloud access must be explicit and separable from local evidence/data.
- Evidence and citations must remain traceable.
- Automated changes should be testable and reversible.
- Safety-related actions must use explicit state transitions and guardrails.
- No bank-account or unrelated credential access.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
newtool health
```

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
pytest
newtool health
```

## Status

**Phase 0 — project skeleton.**

The repository is ready for incremental development. The next recommended task is implementing the provider/configuration health-check layer before adding real RAG or safety automation.
