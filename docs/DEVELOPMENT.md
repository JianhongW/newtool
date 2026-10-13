# Development guide

## Initial setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
cp config.example.yaml config.yaml
pytest
newtool health
```

## Current boundaries

The repository currently contains only the reusable project skeleton.

- No production Chroma writes are performed.
- No cloud provider is enabled by default.
- No safety notification or emergency action is enabled.
- No credentials should be committed.
- New functionality should include tests before it becomes a default workflow.

## Suggested next implementation sequence

1. Provider/configuration health checks.
2. Ollama provider interface.
3. Retrieval/evidence types.
4. Read-only RAG query path.
5. Safety event/state model.
6. Android/Windows transport.
7. Controlled learning/event journal.
