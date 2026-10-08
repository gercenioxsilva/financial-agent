import numpy as np
import pandas as pd

TRADING_DAYS = 252

def returns(prices: pd.Series) -> pd.Series:
    return prices.pct_change().dropna()

def annualized_volatility(asset_returns: pd.Series, periods: int = TRADING_DAYS) -> float:
    return float(asset_returns.std(ddof=1) * np.sqrt(periods))

def max_drawdown(prices: pd.Series) -> float:
    running_max = prices.cummax()
    drawdown = prices / running_max - 1.0
    return float(drawdown.min())

def sharpe_ratio(asset_returns: pd.Series, risk_free_annual: float = 0.0, periods: int = TRADING_DAYS) -> float:
    if asset_returns.std(ddof=1) == 0:
        return 0.0
    rf_period = (1 + risk_free_annual) ** (1 / periods) - 1
    excess = asset_returns - rf_period
    return float(excess.mean() / asset_returns.std(ddof=1) * np.sqrt(periods))

def historical_var(asset_returns: pd.Series, confidence: float = 0.95) -> float:
    return float(np.quantile(asset_returns.dropna(), 1 - confidence))
