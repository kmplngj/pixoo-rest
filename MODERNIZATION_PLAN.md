# Project Structure Modernization Plan

## Current Structure Analysis

### Current Layout (Flat Layout)
```
pixoo-rest/
├── app.py                    # Main application file
├── _helpers.py               # Helper utilities
├── swag/                     # Swagger definitions
│   ├── __init__.py
│   ├── definitions.py
│   ├── passthrough.py
│   ├── duck.gif
│   └── [endpoint yamls]
├── examples/                 # Example scripts
├── requirements.txt          # Legacy (deprecated)
├── pyproject.toml           # Modern config ✓
├── compose.yml              # Docker compose
├── Dockerfile               # Container config
└── version.txt              # Version file (deprecated)
```

### Issues with Current Structure

1. **❌ Flat Layout**: Source code at root level mixes with config files
2. **❌ Poor Module Organization**: All code in root (app.py, _helpers.py)
3. **❌ No Tests Directory**: No dedicated test structure
4. **❌ Inconsistent Naming**: `_helpers.py` uses private naming convention incorrectly
5. **❌ Mixed Concerns**: Static assets (duck.gif) in code directory (swag/)
6. **❌ No Entry Points**: No proper CLI entry point definition in pyproject.toml
7. **❌ Version in File**: version.txt instead of single source in pyproject.toml
8. **❌ No Documentation Structure**: No docs/ directory for organized documentation

## Recommended Structure (src Layout)

### Target Layout - Modern Python Best Practices
```
pixoo-rest/
├── src/
│   └── pixoo_rest/           # Main package
│       ├── __init__.py       # Package initialization, version
│       ├── __main__.py       # Entry point for python -m pixoo_rest
│       ├── app.py            # Flask application factory
│       ├── cli.py            # CLI entry point
│       ├── config.py         # Configuration management
│       ├── utils.py          # Utility functions (was _helpers.py)
│       ├── api/              # API endpoints module
│       │   ├── __init__.py
│       │   ├── routes.py     # Main route definitions
│       │   └── swagger.py    # Swagger configuration
│       └── swagger_specs/    # Swagger YAML definitions (was swag/)
│           ├── __init__.py
│           ├── definitions.py
│           ├── passthrough.py
│           ├── divoom/
│           ├── download/
│           ├── draw/
│           ├── send/
│           └── set/
├── tests/                    # Test suite
│   ├── __init__.py
│   ├── conftest.py          # Pytest configuration
│   ├── test_app.py
│   ├── test_utils.py
│   └── api/
│       ├── __init__.py
│       └── test_routes.py
├── docs/                     # Documentation
│   ├── index.md
│   ├── api.md
│   ├── deployment.md
│   └── examples.md
├── examples/                 # Example scripts (keep)
│   ├── README.md
│   ├── clockwise_swipe.sh
│   ├── progress_bar.sh
│   └── text_download.json
├── static/                   # Static assets
│   ├── duck.gif
│   └── screenshot.png
├── pyproject.toml           # Project configuration ✓
├── uv.lock                  # Dependency lock ✓
├── compose.yml              # Docker compose ✓
├── Dockerfile               # Container config ✓
├── .dockerignore            # Docker ignore ✓
├── .gitignore               # Git ignore ✓
├── README.md                # Main documentation ✓
├── CHANGELOG.md             # Changelog ✓
├── LICENSE                  # License ✓
└── agents.md                # AI agents doc ✓
```

## Migration Steps

### Phase 1: Create src Layout Structure
1. Create `src/pixoo_rest/` directory structure
2. Move `app.py` to `src/pixoo_rest/app.py`
3. Rename and move `_helpers.py` to `src/pixoo_rest/utils.py`
4. Rename and move `swag/` to `src/pixoo_rest/swagger_specs/`
5. Create `src/pixoo_rest/__init__.py` with version
6. Create `src/pixoo_rest/__main__.py` for CLI entry point

### Phase 2: Add Entry Points and Configuration
1. Add `[project.scripts]` section to `pyproject.toml`
2. Add `[project.entry-points]` for Flask app
3. Update imports throughout the codebase
4. Create `src/pixoo_rest/config.py` for configuration management
5. Remove `version.txt` dependency

### Phase 3: Create Test Structure
1. Create `tests/` directory with proper structure
2. Add `conftest.py` for pytest fixtures
3. Create initial test files
4. Update pyproject.toml with test configuration

### Phase 4: Organize Assets and Documentation
1. Create `static/` directory
2. Move `duck.gif` and `screenshot.png` to `static/`
3. Create `docs/` directory
4. Move relevant README sections to docs

### Phase 5: Update Build Configuration
1. Update Dockerfile to use src layout
2. Update compose.yml if needed
3. Update .dockerignore
4. Add proper build backend configuration
5. Test uv sync and uv run

### Phase 6: Update Import Paths
1. Update all internal imports to use `pixoo_rest` package
2. Update tests to import from `pixoo_rest`
3. Update examples if they reference the package

## Benefits of New Structure

### 1. **Clear Separation of Concerns**
- Source code in `src/`
- Tests in `tests/`
- Documentation in `docs/`
- Examples remain clear
- Static assets in `static/`

### 2. **Avoid Import Conflicts**
- `src/` layout prevents pytest from accidentally importing from wrong location
- Package name clearly defined
- No ambiguity about what's importable

### 3. **Better Packaging**
- Proper package structure for distribution
- Can install with `pip install -e .`
- Works well with `uv` package manager
- Entry points properly defined

### 4. **Professional Standards**
- Follows PEP 517/518 recommendations
- Matches modern Python project conventions
- Similar to popular projects (FastAPI, Flask extensions, etc.)

### 5. **Improved Maintainability**
- Clear module boundaries
- Easy to find code
- Logical organization
- Better IDE support

### 6. **Testing Benefits**
- Clear test organization
- Proper test isolation
- Easy to run specific test suites
- Coverage reporting easier

## Breaking Changes

### Version Bump: 2.0.0 (Major)
This is a major version bump due to:
1. **Import path changes**: Anyone importing the package will need to update
2. **Entry point changes**: CLI commands will change
3. **File structure changes**: Custom deployments may need updates

### Migration Guide for Users
```python
# Old (v1.x)
from swag import definitions
import _helpers

# New (v2.0)
from pixoo_rest.swagger_specs import definitions
from pixoo_rest import utils

# CLI
# Old: python app.py
# New: uv run pixoo-rest
#  or: python -m pixoo_rest
```

## Phase 7: Migrate from Flask to FastAPI

### Why FastAPI?

1. **Modern async/await support** - Better performance for I/O-bound operations
2. **Automatic API documentation** - OpenAPI/Swagger built-in (already using Flasgger)
3. **Type safety with Pydantic** - Runtime validation and IDE support
4. **Better performance** - Up to 3x faster than Flask in benchmarks
5. **Dependency injection** - Clean, testable code
6. **HTTP/2 & HTTP/3 ready** - Modern protocol support

### Migration Strategy

#### 1. Replace Flask with FastAPI
```python
# Old (Flask)
from flask import Flask, request
app = Flask(__name__)

@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id: str):
    return {'item_id': item_id}

# New (FastAPI)
from fastapi import FastAPI, Path
app = FastAPI()

@app.get('/items/{item_id}')
async def get_item(item_id: str = Path(...)):
    return {'item_id': item_id}
```

#### 2. Use Pydantic Models for Request/Response
```python
# src/pixoo_rest/models.py
from pydantic import BaseModel, Field

class ImageUploadRequest(BaseModel):
    url: str = Field(..., description="Image URL to download")
    push_immediately: bool = Field(True, description="Push to device immediately")

class PixooResponse(BaseModel):
    success: bool
    message: str
```

#### 3. Use Pydantic Settings for Configuration
```python
# src/pixoo_rest/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_prefix='PIXOO_'
    )
    
    # Pixoo device settings
    host: str = 'Pixoo64'
    screen_size: int = 64
    debug: bool = False
    test_connection_retries: int = 999999
    
    # REST API settings
    rest_debug: bool = False
    rest_host: str = '127.0.0.1'
    rest_port: int = 5000
    
    # Advanced settings
    script_name: str = ''  # WSGI base path

@lru_cache()
def get_settings() -> Settings:
    return Settings()
```

#### 4. Use APIRouter for Modular Structure
```python
# src/pixoo_rest/api/routers/draw.py
from fastapi import APIRouter, Depends
from pixoo_rest.config import Settings, get_settings

router = APIRouter(prefix="/draw", tags=["drawing"])

@router.post("/pixel")
async def draw_pixel(
    x: int,
    y: int,
    color: str,
    settings: Settings = Depends(get_settings)
):
    # Implementation
    return {"success": True}
```

#### 5. Replace requests with niquests
```python
# Old
import requests
response = requests.get(url)

# New (sync)
import niquests
response = niquests.get(url)

# New (async - preferred)
async with niquests.AsyncSession() as session:
    response = await session.get(url)
```

### New Project Structure with FastAPI

```
pixoo-rest/
├── src/
│   └── pixoo_rest/
│       ├── __init__.py
│       ├── __main__.py
│       ├── main.py              # FastAPI app factory
│       ├── config.py            # Pydantic Settings
│       ├── dependencies.py      # FastAPI dependencies
│       ├── models/              # Pydantic models
│       │   ├── __init__.py
│       │   ├── requests.py      # Request models
│       │   └── responses.py     # Response models
│       ├── api/
│       │   ├── __init__.py
│       │   ├── routers/
│       │   │   ├── __init__.py
│       │   │   ├── draw.py      # Drawing endpoints
│       │   │   ├── send.py      # Send endpoints
│       │   │   ├── set.py       # Settings endpoints
│       │   │   ├── download.py  # Download endpoints
│       │   │   └── divoom.py    # Divoom API endpoints
│       │   └── deps.py          # Route dependencies
│       ├── core/
│       │   ├── __init__.py
│       │   ├── pixoo_client.py  # Pixoo device client
│       │   └── http_client.py   # niquests async client
│       └── utils/
│           ├── __init__.py
│           └── helpers.py       # Utility functions
├── tests/
├── docs/
└── [config files]
```

### Migration Checklist - Phase 7

- [ ] Install FastAPI, Pydantic Settings, niquests
- [ ] Create Pydantic Settings class for configuration
- [ ] Create Pydantic models for request/response validation
- [ ] Convert Flask routes to FastAPI routers
- [ ] Implement dependency injection for Pixoo client
- [ ] Replace requests with niquests AsyncSession
- [ ] Update Swagger/OpenAPI documentation
- [ ] Add async/await throughout codebase
- [ ] Update tests for FastAPI TestClient
- [ ] Update Dockerfile with FastAPI startup command

### Breaking Changes (v2.0.0)

#### API Changes
- **Async by default** - All endpoints now async
- **Type validation** - Invalid data returns 422 instead of 400
- **Response models** - Consistent response structure
- **Error handling** - FastAPI's automatic validation errors

#### Configuration Changes
- **Environment variables** - Unified `PIXOO_` prefix
- **Settings management** - Pydantic Settings instead of os.environ
- **No more dotenv manual loading** - Automatic via Pydantic Settings

#### Performance Improvements
- **HTTP/2 support** - Via uvicorn/niquests
- **Async I/O** - Better concurrent request handling
- **Connection pooling** - Efficient resource usage with niquests

## Implementation Checklist

- [ ] Phase 1: Create src layout structure
- [ ] Phase 2: Add entry points and configuration
- [ ] Phase 3: Create test structure
- [ ] Phase 4: Organize assets and documentation
- [ ] Phase 5: Update build configuration
- [ ] Phase 6: Update import paths
- [ ] **Phase 7: Migrate Flask → FastAPI**
- [ ] **Phase 7a: Install dependencies (FastAPI, Pydantic Settings, niquests)**
- [ ] **Phase 7b: Create Pydantic models and settings**
- [ ] **Phase 7c: Convert Flask routes to FastAPI routers**
- [ ] **Phase 7d: Implement dependency injection**
- [ ] **Phase 7e: Replace requests with niquests**
- [ ] **Phase 7f: Add async/await support**
- [ ] **Phase 7g: Update tests for FastAPI**
- [ ] Update CHANGELOG.md with v2.0.0
- [ ] Update README.md with new structure info
- [ ] Test all functionality
- [ ] Update Docker image
- [ ] Create migration guide
- [ ] Tag v2.0.0 release

## Timeline

- **Phase 1-2**: 1-2 hours (structure + config)
- **Phase 3-4**: 1 hour (tests + docs)
- **Phase 5-6**: 1-2 hours (build + imports)
- **Phase 7**: 3-4 hours (Flask → FastAPI migration)
- **Testing**: 2 hours (expanded for async testing)
- **Documentation**: 1-2 hours (API docs + migration guide)

**Total Estimate**: 9-13 hours of work

## Dependencies Update

### Remove
- `flask` - Replaced by FastAPI
- `requests` - Replaced by niquests
- `flasgger` - FastAPI has built-in OpenAPI

### Add
- `fastapi>=0.115.0` - Modern async web framework
- `uvicorn[standard]>=0.30.0` - ASGI server with HTTP/2 support
- `pydantic>=2.9.0` - Data validation (comes with FastAPI)
- `pydantic-settings>=2.5.0` - Settings management
- `niquests>=3.9.0` - Modern HTTP client with HTTP/2/3 support

### Keep
- `pixoo>=0.9.2` - Pixoo device library
- `python-dotenv>=1.0.1` - .env file support (optional with Pydantic Settings)
- `pillow>=10.4.0` - Image processing
- `gunicorn>=23.0.0` - Production WSGI server (keep for compatibility)

## References

- [Python Packaging User Guide - src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- [PEP 517 - Build Backend](https://peps.python.org/pep-0517/)
- [PEP 518 - pyproject.toml](https://peps.python.org/pep-0518/)
- [Flask Application Factories](https://flask.palletsprojects.com/en/latest/patterns/appfactories/)
- [python-blueprint](https://github.com/johnthagen/python-blueprint) - Modern Python project example
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Official FastAPI docs
- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices) - Community best practices
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) - Settings management
- [niquests Documentation](https://niquests.readthedocs.io/) - Modern HTTP client
- [FastAPI Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) - Application structure
