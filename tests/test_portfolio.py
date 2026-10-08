from src.portfolio.models import PositionInput
from src.portfolio.service import analyze_portfolio
from src.portfolio.projection import project_wealth

def test_portfolio_analysis():
    result = analyze_portfolio([
        PositionInput(symbol="AAA", quantity=10, average_price=10, current_price=12),
        PositionInput(symbol="BBB", quantity=5, average_price=20, current_price=18),
    ])
    assert result.invested_value == 200
    assert result.market_value == 210
    assert result.unrealized_pnl == 10
    assert round(sum(p.weight for p in result.positions), 8) == 1.0

def test_projection_grows_with_positive_return_and_contributions():
    value = project_wealth(10000, 1000, 0.08, 1)
    assert value > 22000
