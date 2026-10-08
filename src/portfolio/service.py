from .models import PositionInput, PositionAnalysis, PortfolioAnalysis

def analyze_portfolio(positions: list[PositionInput]) -> PortfolioAnalysis:
    if not positions:
        return PortfolioAnalysis(invested_value=0, market_value=0, unrealized_pnl=0, return_pct=0, positions=[])

    invested = sum(p.quantity * p.average_price for p in positions)
    market = sum(p.quantity * p.current_price for p in positions)
    pnl = market - invested
    return_pct = (pnl / invested) if invested else 0.0

    rows = []
    for p in positions:
        position_invested = p.quantity * p.average_price
        position_market = p.quantity * p.current_price
        position_pnl = position_market - position_invested
        rows.append(PositionAnalysis(
            symbol=p.symbol.upper(),
            invested_value=round(position_invested, 2),
            market_value=round(position_market, 2),
            unrealized_pnl=round(position_pnl, 2),
            return_pct=position_pnl / position_invested if position_invested else 0.0,
            weight=position_market / market if market else 0.0,
        ))

    return PortfolioAnalysis(
        invested_value=round(invested, 2),
        market_value=round(market, 2),
        unrealized_pnl=round(pnl, 2),
        return_pct=return_pct,
        positions=rows,
    )
