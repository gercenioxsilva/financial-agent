from datetime import UTC, date, datetime
import pandas as pd
from src.market.models import Quote

class MockMarketDataProvider:
    """Development-only provider. Values are synthetic and must never be presented as live market data."""

    async def get_quote(self, symbol: str) -> Quote:
        return Quote(
            symbol=symbol.upper(),
            price=100.0,
            currency="BRL",
            market="MOCK",
            timestamp=datetime.now(UTC),
            provider="mock",
            delayed=True,
        )

    async def get_history(self, symbol: str, start: date, end: date) -> pd.DataFrame:
        index = pd.date_range(start=start, end=end, freq="B")
        return pd.DataFrame({"close": [100.0] * len(index)}, index=index)
