---
description: A systematic stock-analysis framework — valuation models run over 500+ stocks.
---

# Systematic Investment Analysis Framework

**April 2025 - Present**

📚 **[Documentation](https://rubenayla.github.io/invest/)** | 💻 **[GitHub](https://github.com/rubenayla/invest)**

## Overview

A configuration-driven, objective approach to investment analysis that eliminates conversational bias and provides consistent, reproducible results. This framework applies systematic methodology to stock screening and valuation, combining traditional financial models with machine learning predictions.

The system processes entire market indices (S&P 500) through a comprehensive 5-step analysis pipeline: Quality → Value → Growth → Risk → Valuation, providing investors with disciplined, objective stock analysis.

## Key Features

- **AI-Powered Predictions** - LSTM/Transformer neural network with 78.64% directional accuracy
- **Systematic Methodology** - Identical analysis steps for every stock, eliminating human bias
- **Static HTML Dashboard** - Fast, clean interface with real-time valuations
- **Configurable Analysis** - Define investment criteria via YAML configuration files
- **Multiple Valuation Models** - DCF, Enhanced DCF, Growth DCF, RIM, Simple Ratios
- **Comprehensive Screening** - Quality, value, growth, and risk dimensions
- **Scalable** - Analyze individual stocks or entire market indices

## Technical Details

### System Architecture

**5-Step Analysis Pipeline:**
1. **Quality Assessment** - Financial strength and stability metrics
2. **Value Analysis** - Valuation attractiveness evaluation
3. **Growth Evaluation** - Business expansion prospects
4. **Risk Assessment** - Financial and business risk factors
5. **Valuation Models** - Intrinsic value calculations (DCF, RIM)

**Data Infrastructure:**
- 1.4GB SQLite database with fundamental data
- 3,534 historical snapshots (2006-2023)
- 92-100% feature coverage for ML models

### Technologies Used

- **Python 3.12+** - Core implementation
- **uv** - Modern dependency management
- **pandas** - Data manipulation and analysis
- **pydantic** - Configuration validation and schema management
- **yfinance** - Real-time stock data and financials
- **PyYAML** - Configuration file parsing
- **SQLite** - Fundamental data storage
- **LSTM/Transformer** - Neural network for predictions
- **MkDocs** - Documentation system

### Machine Learning Model

- **Architecture:** LSTM/Transformer hybrid with Monte Carlo Dropout
- **Performance:** 78.64% hit rate, 44.2% correlation, 23.05% MAE
- **Training Data:** 3,534 company snapshots spanning 17 years
- **Predictions:** Single-horizon (1-year) forecasts with confidence intervals
- **Production-Ready:** Deployed with complete validation pipeline

## Highlights

!!! success "Systematic Analysis"
    Eliminates conversational AI bias through consistent, reproducible methodology. Same inputs always produce identical outputs, ensuring objectivity in investment decisions.

!!! info "AI-Powered Insights"
    Neural network model achieves 78.64% directional accuracy, combining traditional fundamental analysis with machine learning predictions for comprehensive stock evaluation.

!!! note "Production System"
    Complete end-to-end framework from data fetching to HTML dashboard generation, processing 500+ stocks in 10-15 minutes with detailed reporting.

## Use Cases

- **Value Investing** - Conservative screening for undervalued stocks
- **Growth Focus** - Aggressive screening for high-growth opportunities
- **Market Analysis** - Full S&P 500 screening and comparison
- **Research** - Reproducible analysis for academic or professional use

## Resources

- [Live Documentation](https://rubenayla.github.io/invest/) - Complete user and developer guides
- [GitHub Repository](https://github.com/rubenayla/invest) - Source code and configurations

## Technical Achievements

- Processed and analyzed 500+ S&P 500 stocks systematically
- Built production ML pipeline with 17 years of historical data
- Created static HTML dashboard with multiple valuation models
- Implemented configurable screening with YAML-based criteria
- Developed comprehensive DCF and RIM valuation engines
