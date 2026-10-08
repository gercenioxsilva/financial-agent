---
name: market-data
description: Retrieve and normalize current and historical financial market data.
---
# Market Data Skill
Use whenever the task needs current price, historical OHLCV, dividends, FX, indices, rates or economic indicators.

Required normalized fields:
- symbol
- asset_type
- market
- currency
- value/price
- timestamp
- provider
- delayed/freshness

Never estimate current data. Warn about stale data, missing timestamps, invalid symbols and provider conflicts.
