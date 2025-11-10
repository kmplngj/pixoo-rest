# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-11-10

### 🎉 Major Rewrite - FastAPI Migration

This release represents a complete rewrite of the application using **FastAPI** instead of Flask, bringing modern async capabilities, automatic API documentation, and improved performance.

### Added
- ⚡ **FastAPI framework** with full async/await support
- 📝 **Automatic OpenAPI documentation** (Swagger UI at `/docs`, ReDoc at `/redoc`)
- ✅ **Pydantic v2 validation** for all request/response models
- 🔄 **Async HTTP calls** with httpx for better performance
- 📦 **File upload support** for images and GIFs with FastAPI's UploadFile
- 🌐 **URL download support** for images and GIFs with redirect following
- 🏗️ **Dependency injection** pattern for cleaner code architecture
- 🎯 **Type hints** throughout the codebase for better IDE support
- 🔌 **Centralized dependencies** module for shared resources
- 📊 **Structured logging** with connection status and health checks
- 🎨 **Modern project structure** with src layout (`src/pixoo_rest/`)
- ⚙️ **Pydantic Settings** for environment variable management
- 🧪 **Better error handling** with proper exception chaining

### Changed
- **BREAKING**: Migrated from Flask to FastAPI
- **BREAKING**: All endpoints now use JSON request bodies instead of form data (except file uploads)
- **BREAKING**: Response format now follows FastAPI/Pydantic schema (status, message fields)
- **BREAKING**: Minimum Python version now `>=3.10` (required for modern type hints)
- **BREAKING**: Entry point changed from `app.py` to `pixoo-rest` command or `python -m pixoo_rest.app`
- Reorganized code into modular routers (`draw`, `send`, `set`, `image`, `download`, `divoom`)
- Improved configuration with Pydantic Settings and better environment variable handling
- Enhanced GIF handling with async frame processing
- Updated all dependencies to their latest versions
- Modernized development workflow with uv package manager

### Dependencies
- Added: `fastapi>=0.115.0`
- Added: `uvicorn[standard]>=0.30.0` (ASGI server)
- Added: `pydantic>=2.9.0` (validation)
- Added: `pydantic-settings>=2.5.0` (config management)
- Added: `httpx>=0.28.0` (async HTTP client)
- Added: `python-multipart>=0.0.20` (file upload support)
- Removed: `flask` and related Flask dependencies
- Removed: `flasgger` (replaced by FastAPI's built-in OpenAPI)
- Removed: `requests` (replaced by async httpx)
- Removed: `python-dotenv` (Pydantic Settings handles .env)

### Migration Guide

#### Environment Variables
No changes to environment variable names - all existing `.env` files work as-is:
- `PIXOO_HOST` - Device hostname or IP
- `PIXOO_SCREEN_SIZE` - Screen size (16, 32, or 64)
- `PIXOO_DEBUG` - Debug mode for pixoo library
- `PIXOO_REST_HOST` - Server listen address
- `PIXOO_REST_PORT` - Server port
- `PIXOO_TEST_CONNECTION_RETRIES` - Connection retry count

#### API Changes
All endpoint paths remain the same, but request format has changed:

**Old (Flask - form data):**
```bash
curl -X POST http://localhost:5000/pixel \
  -F "x=10" -F "y=10" -F "r=255" -F "g=0" -F "b=0"
```

**New (FastAPI - JSON):**
```bash
curl -X POST http://localhost:5000/draw/pixel \
  -H "Content-Type: application/json" \
  -d '{"x": 10, "y": 10, "r": 255, "g": 0, "b": 0, "push_immediately": true}'
```

#### Running the App
**Old:**
```bash
python app.py
```

**New:**
```bash
uv run pixoo-rest
# or
python -m pixoo_rest.app
```

#### API Documentation
- Old: Swagger UI at `/` (redirect to `/apidocs`)
- New: Swagger UI at `/docs`, ReDoc at `/redoc`, root info at `/`

### Removed
- Flask application and all Flask-specific code
- Flasgger for Swagger generation (now built into FastAPI)
- Custom Swagger spec YAML files (FastAPI generates OpenAPI automatically)
- Legacy passthrough endpoint format
- `SCRIPT_NAME` environment variable support (use reverse proxy path rewriting instead)

## [1.7.0] - 2025-11-09

### Added
- Modern `pyproject.toml` with PEP 621 compliant metadata
- Support for `uv` package manager for faster dependency resolution
- `agents.md` documentation for AI-assisted development workflow
- Development dependencies group (pytest, black, ruff, mypy)
- Proper project classifiers and URLs in package metadata
- Enhanced `/image` endpoint that accepts both file uploads and image URLs

### Changed
- Migrated from `requirements.txt` to `pyproject.toml` for dependency management
- Adopted Semantic Versioning 2.0.0
- **BREAKING**: Updated minimum Python version requirement to `>=3.10` (required by pixoo dependency)
- Improved project structure following modern Python standards
- Updated CHANGELOG format to follow Keep a Changelog standard
- Modernized Dockerfile to use Python 3.12 and uv package manager

### Deprecated
- `requirements.txt` (use `pyproject.toml` instead)
- `version.txt` (version now managed in `pyproject.toml`)

### Removed
- Legacy `requirements.txt` workflow in favor of `pyproject.toml`
- Helm chart directory (no longer supported)
- Renamed `docker-compose.yml` to `compose.yml` (modern Docker Compose naming)

## [1.6.0] - 2024-08-28

* removed `pixoo` as git-submodule; now added via PyPi package
* other dependencies updated

## 1.5.1 (2024-05-09)

* improved configuration options when running behind a reverse proxy:  
  the `SCRIPT_NAME` environment variable (see [WSGI docs](https://wsgi.readthedocs.io/en/latest/definitions.html#envvar-SCRIPT_NAME)) is now taken into consideration; making it possible to set a custom base-path

## 1.5.0 (2024-05-06)

* new: (passthrough-)endpoint `sendHttpItemList`, which is available with the latest firmware update and offers drawing of multiple text-elements at once
* new: custom `download/text` endpoint
* new: Helm charts / K8s
* improved handling for GIF file upload (automatically limit to 59 frames; following the restriction of the device/API)
* updated dependencies
* other minor improvements

## 1.4.2 (2024-02-10)

* updated dependencies
* minor improvements (Dockerfile, docker-compose, log output, etc.)

## 1.4.1 (2023-10-16)

* updated dependencies
* minor improvements

## 1.4.0 (2023-07-23)

* new "download" endpoints (automatically download and send images to your Pixoo)

## 1.3.4 (2023-06-26)

* dependency updates

## 1.3.3 (2023-05-06)

* dependency updates

## 1.3.2 (2023-03-21)

* fix dependency conflict (_flasgger_ requires _Pillow_ 9.2.0)

## 1.3.1 (2023-03-21)

* dependency updates
* "restart" directive removed from [docker-compose.yml](docker-compose.yml) 

## 1.3.0 (2023-01-06)

* new: 'divoom' section (query official [API](https://app.divoom-gz.com))
* dependency updates
* other minor improvements

## 1.2.0 (2022-10-29)

* new environment settings `PIXOO_REST_HOST` and `PIXOO_REST_DEBUG` (see [README](README.md))
* new passthrough-commands:
  * GetDeviceTime
  * SetDisTempMode
  * SetTime24Flag
  * setHighLightMode
  * SetWhiteBalance
  * GetWeatherInfo
  * PlayBuzzer
* other minor improvements

## 1.1.0 (2022-10-05)

* improved [Dockerfile](Dockerfile) (checkout of the pixoo-library's explicit commit-hash; which should correlate with the git-submodule and pin the actual dependencies)
* new `screen/on/{true|false}` endpoint
* new passthrough-commands:
  * SetScreenRotationAngle
  * SetMirrorMode
* other minor improvements

## 1.0.0 (2022-03-05)

* initial release