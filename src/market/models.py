from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field

class AssetType(str, Enum):
    STOCK = "stock"
    ETF = "etf"
    FII = "fii"
    BOND = "bond"
    FUND = "fund"
    CRYPTO = "crypto"
    CURRENCY = "currency"

class Asset(BaseModel):
    symbol: str
    name: str | None = None
    asset_type: AssetType
    exchange: str
    country: str
    currency: str
    sector: str | None = None

class Quote(BaseModel):
    symbol: str
    price: float = Field(gt=0)
    currency: str
    market: str
    timestamp: datetime
    provider: str
    delayed: bool = True
