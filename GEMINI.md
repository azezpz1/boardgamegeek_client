# Gemini Project Guidelines

## Project Purpose

This project is a Python wrapper for the boardgamegeek.com XML API. It aims to use modern Python techniques and structures for easy integration into other Python packages.

## Key Principles

- **Modern Python:** Utilize modern Python features and best practices.
- **Thorough Testing:** Comprehensive unit and integration tests are required.
- **Domain-Driven Design:** Adhere to DDD principles in the software design.
- **Type Hinting:** All code must include type hints.

## Development Workflow

When making changes, please run the following tools to ensure consistency and quality:

- `black .`
- `ruff . --fix`
- `mypy .`
- `pytest`

## BoardGameGeek API

The XML API2 endpoint for retrieving board game data is: `https://boardgamegeek.com/xmlapi2/thing?id={bgg_id}`
