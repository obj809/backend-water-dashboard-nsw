# NSW Water Dashboard Backend API

![tests-backend](https://github.com/obj809/backend-water-dashboard-nsw/actions/workflows/ci.yml/badge.svg)

## Project Overview

A Flask REST API backend providing dam storage and water resource data for New South Wales, Australia. The API delivers real-time and historical water data including storage levels, inflow/release metrics, and multi-year trend analysis across NSW dam systems.

## Screenshot
![Application Screenshot](screenshots/documentation-light.png "Swagger API Documentation")

## Table of Contents
- [Goals & MVP](#goals--mvp)
- [Tech Stack](#tech-stack)
- [How To Use](#how-to-use)
- [Design Goals](#design-goals)
- [Project Features](#project-features)
- [Additions & Improvements](#additions--improvements)
- [Learning Highlights](#learning-highlights)
- [Known Issues](#known-issues)
- [Challenges](#challenges)
- [Contact Me](#contact-me)

## Goals & MVP

Build a robust REST API for NSW dam and water resource data that supports real-time storage monitoring, historical data queries with date filtering, and analytical insights including 12-month, 5-year, and 20-year averages across grouped dam systems.

## Tech Stack

- Flask 3.1
- Flask-RESTX
- Flask-SQLAlchemy
- Flask-Migrate
- PostgreSQL / MySQL
- pytest
- Gunicorn
- Render

## How To Use

1. Clone the repository and install dependencies:
```bash
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

2. Configure your `.env` file with database credentials and run:
```bash
python run.py
```

3. Access the API documentation at `http://localhost:5001/api/docs`

## Design Goals

- **RESTful Architecture**: Clean, predictable API design following REST principles
- **Automatic Documentation**: Self-documenting API with interactive Swagger UI
- **Database Flexibility**: Support for multiple database backends (MySQL, PostgreSQL)
- **Test-Driven Development**: Comprehensive test suite with high code coverage

## Project Features

- [x] Dam management with CRUD operations and geolocation data
- [x] Real-time storage level snapshots for all dams
- [x] Historical time-series data with date filtering
- [x] Multi-period analysis (12-month, 5-year, 20-year averages)
- [x] Regional dam grouping (e.g., Sydney water system)
- [x] Interactive Swagger UI documentation
- [x] Automated CI/CD with GitHub Actions

## Additions & Improvements

- [ ] Pagination support for large datasets
- [ ] Rate limiting and API authentication
- [ ] Real-time WebSocket updates
- [ ] Docker containerization

## Learning Highlights
- Implementing automatic API documentation with Flask-RESTX and Swagger UI
- Designing complex SQLAlchemy relationships (one-to-one, one-to-many, many-to-many)
- Building comprehensive pytest test suites with in-memory SQLite for test isolation
- Implementing multi-database support with environment-based configuration

## Known Issues

- Large dataset queries without pagination may cause performance issues

## Challenges

### Multi-Database Support
**Challenge**: Supporting both MySQL (local) and PostgreSQL (production) with different connection formats.

**Solution**: Implemented flexible configuration with `DB_PROVIDER` environment variable and SQLAlchemy's database-agnostic ORM.

### Composite Primary Keys
**Challenge**: SpecificDamAnalysis uses composite primary key (dam_id, analysis_date) requiring special Flask-RESTX handling.

**Solution**: Created custom route parameters and date parsing utilities for proper database queries.

## Contact Me
- Visit my [LinkedIn](https://www.linkedin.com/in/obj809/) for more details.
- Check out my [GitHub](https://github.com/cyberforge1) for more projects.
- Or send me an email at obj809@gmail.com
<br />
Thanks for your interest in this project. Feel free to reach out with any thoughts or questions.
<br />
<br />
Oliver Jenkins © 2024