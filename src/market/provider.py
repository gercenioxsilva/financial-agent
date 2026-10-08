from datetime import date
from typing import Protocol
import pandas as pd
from .models import Quote

class MarketDataProvider(Protocol):
    async def get_quote(self, symbol: str) -> Quote: ...
    async def get_history(self, symbol: str, start: date, end: date) -> pd.DataFrame: ...
