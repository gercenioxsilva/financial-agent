def project_wealth(initial_capital: float, monthly_contribution: float, annual_return: float, years: int) -> float:
    """Hypothetical projection using a constant annual return assumption."""
    months = years * 12
    monthly_rate = (1 + annual_return) ** (1 / 12) - 1
    balance = initial_capital
    for _ in range(months):
        balance = balance * (1 + monthly_rate) + monthly_contribution
    return round(balance, 2)
