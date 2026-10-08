from pydantic import BaseModel, Field

class PositionInput(BaseModel):
    symbol: str
    quantity: float = Field(gt=0)
    average_price: float = Field(gt=0)
    current_price: float = Field(gt=0)
    currency: str = "BRL"

class PositionAnalysis(BaseModel):
    symbol: str
    invested_value: float
    market_value: float
    unrealized_pnl: float
    return_pct: float
    weight: float

class PortfolioAnalysis(BaseModel):
    invested_value: float
    market_value: float
    unrealized_pnl: float
    return_pct: float
    positions: list[PositionAnalysis]
