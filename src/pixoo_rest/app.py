"""FastAPI application for Pixoo REST API."""

import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI
from pixoo import Pixoo

from pixoo_rest.api import divoom, download, draw, image, send, set as set_router
from pixoo_rest.core.config import settings
from pixoo_rest.dependencies import set_pixoo_instance
from pixoo_rest import utils


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager - handles startup and shutdown."""
    # Startup: Initialize Pixoo device
    print(f"Connecting to Pixoo device at {settings.pixoo_host}...")
    
    # Test connection to Pixoo device
    for connection_test_count in range(settings.pixoo_test_connection_retries + 1):
        if utils.try_to_request(f'http://{settings.pixoo_host}/get'):
            break
        else:
            if connection_test_count == settings.pixoo_test_connection_retries:
                sys.exit("ERROR: Failed to connect to Pixoo device.")
            print(f"Connection attempt {connection_test_count + 1} failed, retrying...")
    
    pixoo = Pixoo(settings.pixoo_host, settings.pixoo_screen_size, settings.pixoo_debug)
    print(f"Successfully connected to Pixoo device at {settings.pixoo_host}")
    
    # Set the global pixoo instance
    set_pixoo_instance(pixoo)
    
    yield
    
    # Shutdown: Cleanup if needed
    print("Shutting down...")


# Create FastAPI app
app = FastAPI(
    title="Pixoo REST API",
    description="A RESTful API to easily interact with Wi-Fi enabled Divoom Pixoo devices",
    version="2.0.0",
    lifespan=lifespan,
)

# Include routers
app.include_router(draw.router)
app.include_router(send.router)
app.include_router(set_router.router)
app.include_router(image.router)
app.include_router(download.router)
app.include_router(divoom.router)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "pixoo_host": settings.pixoo_host}


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "Pixoo REST API",
        "version": "2.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
        "openapi": "/openapi.json",
    }


def main():
    """Entry point for the application."""
    import uvicorn
    
    print(f"Starting server on {settings.pixoo_rest_host}:{settings.pixoo_rest_port}")
    print(f"Pixoo device: {settings.pixoo_host}")
    
    uvicorn.run(
        app,
        host=settings.pixoo_rest_host,
        port=settings.pixoo_rest_port,
        log_level="info",
    )


if __name__ == "__main__":
    main()
