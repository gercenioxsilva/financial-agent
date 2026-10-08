# Financial Intelligence Agent

Base project for a GitHub Copilot-powered financial intelligence agent focused on market data, portfolio analysis, risk, macro context, and wealth-growth simulations.

## Goals
- Retrieve fresh market data through pluggable providers.
- Analyze portfolios with deterministic calculations.
- Simulate wealth-growth scenarios without promising returns.
- Separate facts, calculations, assumptions, scenarios, and interpretations.
- Keep LLM orchestration separate from financial math and market-data ingestion.

## Structure
- `.github/agents`: Copilot custom agents.
- `.github/skills`: domain skills.
- `.github/prompts`: reusable task prompts.
- `specs`: feature specifications.
- `src`: Python core for providers, portfolio and risk engines.
- `tests`: automated tests.

## Quick start
```powershell
cd D:\financial-agent
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .[dev]
pytest
uvicorn src.app:app --reload
```

## Important
This project is an analysis and decision-support platform. It must not fabricate market data, promise returns, or present simulations as guarantees.
