"""Shared FastAPI dependencies."""

from fastapi import HTTPException
from pixoo import Pixoo


# Global Pixoo device instance
_pixoo_instance: Pixoo | None = None


def set_pixoo_instance(pixoo_instance: Pixoo) -> None:
    """Set the global Pixoo instance."""
    global _pixoo_instance
    _pixoo_instance = pixoo_instance


def get_pixoo() -> Pixoo:
    """FastAPI dependency that provides the Pixoo instance."""
    if _pixoo_instance is None:
        raise HTTPException(
            status_code=503,
            detail="Pixoo device not initialized"
        )
    return _pixoo_instance
