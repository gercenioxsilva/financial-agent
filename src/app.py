from fastapi import FastAPI
from pydantic import BaseModel
from src.portfolio.models import PositionInput, PortfolioAnalysis
from src.portfolio.service import analyze_portfolio
from src.portfolio.projection import project_wealth

app = FastAPI(title="Financial Intelligence Agent API", version="0.1.0")

class PortfolioRequest(BaseModel):
    positions: list[PositionInput]

class ProjectionRequest(BaseModel):
    initial_capital: float
    monthly_contribution: float
    annual_return: float
    years: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/portfolio/analyze", response_model=PortfolioAnalysis)
def portfolio_analysis(request: PortfolioRequest):
    return analyze_portfolio(request.positions)

@app.post("/portfolio/project")
def portfolio_projection(request: ProjectionRequest):
    return {
        "projected_value": project_wealth(
            request.initial_capital,
            request.monthly_contribution,
            request.annual_return,
            request.years,
        ),
        "assumption": "constant hypothetical annual return; not a guaranteed outcome",
    }
