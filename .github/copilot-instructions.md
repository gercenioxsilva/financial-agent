# Financial Agent - Copilot Instructions

You are working on a financial intelligence platform.

## Engineering principles
- Apply Clean Architecture, SOLID, DDD, Clean Code and explicit boundaries.
- Keep domain logic independent from APIs, providers and frameworks.
- Prefer interfaces/protocols for external market-data providers.
- Use deterministic code for all financial calculations.
- Never let an LLM invent prices, returns, ratios, macro indicators or portfolio metrics.
- Every current-data response must include source and timestamp.
- Preserve backwards compatibility unless a spec explicitly says otherwise.
- Add or update tests for every behavior change.
- Do not hard-code secrets, API keys or credentials.

## Financial safety
- Separate facts, calculations, assumptions, scenarios and interpretations.
- Never claim guaranteed returns.
- Label simulated returns as hypothetical.
- Surface stale, missing or conflicting data.
- Prefer official/regulatory sources when available.

## Architecture
Keep these conceptual layers independent:
1. Domain
2. Application/use cases
3. Infrastructure/providers
4. Delivery/API
5. AI orchestration
