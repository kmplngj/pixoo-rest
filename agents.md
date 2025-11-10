# Agents

This document describes the AI agents and automation involved in this project.

## Project Modernization

This project was refactored and modernized using AI assistance on 2025-11-09.

### Changes Made

- Migrated from `requirements.txt` to modern `pyproject.toml` with `uv` package manager
- Adopted PEP 621 compliant project metadata
- Implemented dependency groups for dev dependencies
- Added proper Python version constraints
- Adopted Semantic Versioning 2.0.0
- Cleaned up legacy configuration files
- Updated build system to use modern standards

### Tools Used

- **UV**: Modern, fast Python package manager and project manager
- **GitHub Copilot**: AI-assisted code refactoring and modernization
- **DeepWiki**: Research on best practices for Python project structure

## Development Workflow

### Adding Dependencies

Use `uv` to manage dependencies:

```bash
# Add a runtime dependency
uv add package-name

# Add a development dependency
uv add --group dev package-name

# Sync the environment
uv sync
```

### Running the Application

```bash
# Run with uv
uv run python app.py

# Or activate the virtual environment
source .venv/bin/activate
python app.py
```

### Updating Dependencies

```bash
# Update all dependencies
uv lock --upgrade

# Update specific package
uv lock --upgrade-package package-name
```

## Version Management

This project follows [Semantic Versioning 2.0.0](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions
- **PATCH** version for backwards-compatible bug fixes

Version is managed in `pyproject.toml` and should be updated in the CHANGELOG.md when releasing.
