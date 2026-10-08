import pandas as pd
from src.risk.metrics import returns, max_drawdown, annualized_volatility, historical_var

def test_risk_metrics():
    prices = pd.Series([100, 110, 105, 120, 90, 100], dtype=float)
    r = returns(prices)
    assert len(r) == 5
    assert max_drawdown(prices) < 0
    assert annualized_volatility(r) > 0
    assert historical_var(r) < 0
