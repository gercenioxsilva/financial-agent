# Market Data Specification

The system SHALL expose provider-independent contracts for quotes and historical prices.
Each result SHALL include symbol, market, currency, timestamp, provider and freshness/delay metadata.
Provider failures SHALL be isolated from domain logic.
