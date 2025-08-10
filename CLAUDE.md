# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains two main projects:

1. **InvestmentAI** - AI-powered investment analysis system for AI/robotics stocks and ETFs
2. **Paraguay Laptop Research** - Laptop research and analysis system for Paraguay's retail market

Both projects focus on automated analysis, data processing, and decision support systems.

## Project Structure

```
ivan/
├── InvestmentAI/                    # AI-powered investment analysis
│   ├── core/investment_system/      # Main Python package
│   ├── config/                      # Configuration files
│   ├── tools/                       # Analysis and monitoring scripts
│   ├── web/                         # Flask web dashboard
│   ├── mcp/                         # MCP server implementations
│   ├── docs/                        # Documentation
│   ├── reports/                     # Generated analysis reports
│   └── cache/                       # Data cache
└── New Laptop/
    └── Paraguay_Laptop_Research/    # Laptop research system
        ├── src/                     # Modular source code
        ├── config/                  # Configuration management
        ├── examples/                # Example results
        └── output/                  # Generated reports
```

## Common Development Commands

### InvestmentAI System

**Analysis Commands:**
```bash
# Quick daily analysis (2-3 minutes)
cd InvestmentAI
python -m core.investment_system.analysis.quick_analysis

# Comprehensive analysis (10-15 minutes)
python -m core.investment_system.analysis.comprehensive_analyzer

# System monitoring
python -m core.investment_system.monitoring.system_monitor

# Windows batch shortcuts
tools\run_daily_analysis.bat
tools\run_comprehensive_analysis.bat
tools\run_system_monitor.bat
```

**Development Commands:**
```bash
# Run tests
python -m pytest tests/ -v
# Or: tools\run_tests.bat

# Code quality (using Makefile)
make format     # Format code with black/isort
make lint       # Run flake8 linting
make type-check # Run mypy type checking
make test       # Run test suite
```

**Web Dashboard:**
```bash
cd web
python app.py
# Access at http://localhost:5000
```

### Paraguay Laptop Research

**Research Commands:**
```bash
cd "New Laptop/Paraguay_Laptop_Research"

# Find Thunderbolt 4 laptops
python laptop_research.py thunderbolt

# Budget analysis
python laptop_research.py budget --min-price 500 --max-price 700

# System overview
python laptop_research.py summary

# Clean old files
python laptop_research.py cleanup --auto-delete
```

**Setup:**
```bash
# Install dependencies
pip install -r requirements.txt

# Setup configuration
cp config/settings_example.py config/settings_personal.py
# Edit settings_personal.py with requirements
```

## Architecture and Design Patterns

### InvestmentAI Architecture

**Layered Architecture:**
- **Data Layer**: Market data collection, news feeds, real-time data
- **Analysis Layer**: Technical analysis, sentiment analysis, AI predictions
- **Portfolio Layer**: Risk management, backtesting, signal generation
- **Monitoring Layer**: System health, alerts, performance tracking
- **Reporting Layer**: Automated reports, visualizations

**Key Components:**
- `core/investment_system/data/market_data_collector.py` - Multi-source data aggregation
- `core/investment_system/analysis/quick_analysis.py` - Fast technical analysis
- `core/investment_system/portfolio/risk_management.py` - Position sizing and risk metrics
- `core/investment_system/monitoring/system_monitor.py` - System health monitoring

**Configuration:**
- Central config: `config/config.json`
- User profile: Ivan, $900 balance, medium risk tolerance
- Target assets: AI/Robotics stocks (NVDA, MSFT, TSLA) and ETFs (KROP, BOTZ, ARKQ)

### Paraguay Laptop Research Architecture

**Modular Design:**
- `src/analysis/` - Compatibility scoring and filtering
- `src/commands/` - CLI command implementations
- `src/models/` - Type-safe data structures
- `src/parsers/` - HTML parsing and data extraction
- `src/utils/` - Shared utilities

**Key Features:**
- Thunderbolt 4 detection for external monitor support
- Gaming laptop exclusion for work-focused results
- Multi-retailer support (Casa Nissei, TiendaMóvil, Shopping China)
- Currency conversion (PYG to USD)

## Important Configuration Files

### InvestmentAI
- `config/config.json` - Central configuration with user profile and API settings
- `pyproject.toml` - Python package configuration with dependencies
- `requirements.txt` - Production dependencies
- `Makefile` - Development commands and workflows

### Paraguay Laptop Research
- `config/settings_personal.py` - Personal configuration (git-ignored)
- `config/settings_example.py` - Template configuration
- `requirements.txt` - Python dependencies

## Testing and Quality

### InvestmentAI
```bash
# Run full test suite
python -m pytest tests/ -v

# Specific test categories
python -m pytest tests/ -m "not slow"  # Quick tests only
python -m pytest tests/ -m "api"       # API tests
python -m pytest tests/ -m "portfolio" # Portfolio tests

# Code quality checks
make format lint type-check test
```

### Paraguay Laptop Research
```bash
# Test installation
python laptop_research.py summary

# Validate configuration
python -c "from config.config_loader import load_config; print('Config loaded successfully')"
```

## Key Dependencies and Requirements

### InvestmentAI
- **Core**: pandas, numpy, requests, yfinance
- **APIs**: twelvedata, alpaca-trade-api, finnhub-python, newsapi-python
- **Interactive Brokers**: ib_insync
- **YouTube API**: google-api-python-client, youtube-transcript-api
- **Web**: Flask (for dashboard)
- **Dev**: pytest, black, isort, flake8, mypy

### Paraguay Laptop Research
- **Web Scraping**: beautifulsoup4, requests, lxml
- **Compression**: brotli (for TiendaMóvil data)

## Investment System Focus Areas

- **Primary Stocks**: NVDA, MSFT, TSLA, DE, TSM, AMZN, GOOGL, META, AAPL, CRM
- **AI/Robotics ETFs**: KROP, BOTZ, SOXX, ARKQ, ROBO, IRBO, UBOT
- **Smart Money Tracking**: ARK Invest, Tiger Global, Coatue, Whale Rock, Berkshire Hathaway
- **Portfolio**: $900 balance, medium risk tolerance, quarterly rebalancing
- **Ethics Screening**: ESG-focused investments, environmental protection

## Import Patterns

### InvestmentAI
```python
# Modern package imports
from core.investment_system.analysis import get_stock_analysis, ComprehensiveAnalyzer
from core.investment_system.portfolio import RiskManager, PortfolioAnalyzer
from core.investment_system.data import MarketDataCollector
from core.investment_system.utils import CacheManager

# Configuration loading
import json
from pathlib import Path
config_path = Path("config/config.json")
with open(config_path, 'r') as f:
    config = json.load(f)
```

### Paraguay Laptop Research
```python
# Modular imports
from src.analysis.compatibility_analyzer import CompatibilityAnalyzer
from src.commands.budget_finder import BudgetFinder
from src.models.laptop import LaptopProduct
from config.config_loader import load_config

# Configuration
config = load_config()  # Automatically loads personal or example config
```

## Development Guidelines

1. **Code Organization**: Follow the established package structure
2. **Configuration**: Use centralized config files, never hardcode values
3. **Testing**: Write tests for new functionality, especially analysis algorithms
4. **Documentation**: Update relevant docs when adding features
5. **Error Handling**: Include comprehensive error handling and logging
6. **Git**: Use meaningful commit messages, don't commit sensitive data

## Special Considerations

### InvestmentAI
- Real money involved - extra validation required
- API rate limits - implement proper caching
- Time-sensitive data - ensure fresh market data
- Risk management - always include confidence scores

### Paraguay Laptop Research
- Local market focus - currency conversion required
- Retailer-specific parsing - handle different HTML formats
- Work-focused filtering - exclude gaming/touchscreen models
- Thunderbolt 4 validation - critical for external monitor support

## MCP Integration

Both projects are optimized for Claude Code MCP integration:

### InvestmentAI MCPs
- `mcp/investment_mcp.py` - Investment analysis server
- `mcp/powerbi_mcp.py` - PowerBI integration
- `mcp/web_dev_mcp.py` - Web dashboard development

### Paraguay Laptop Research
- Filesystem MCP for data analysis
- Browser Tools MCP for web scraping
- Full documentation in `CLAUDE_CODE_INTEGRATION.md`

## Maintenance Tasks

### Daily
- Run investment analysis: `tools\run_daily_analysis.bat`
- Check system health: `make monitor`

### Weekly
- Clean old reports: `make clean-reports`
- Update dependencies: `pip install -r requirements.txt --upgrade`

### Monthly
- Full system analysis: `tools\run_comprehensive_analysis.bat`
- Review and update configurations
- Archive old data and reports