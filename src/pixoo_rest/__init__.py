"""Pixoo REST API - Modern FastAPI implementation."""

try:
    # Try to get version from package metadata (when installed)
    from importlib.metadata import version
    __version__ = version("pixoo-rest")
except Exception:
    # Fallback for development mode
    __version__ = "2.0.0"
