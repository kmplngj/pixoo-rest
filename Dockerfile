FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install system dependencies (including tkinter for pixoo simulator)
RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
        curl \
        python3-tk \
        tk-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependency files first for better layer caching
COPY pyproject.toml uv.lock* ./
COPY README.md .

# Install dependencies using uv
RUN uv sync --frozen --no-dev --no-install-project

# Copy application source code
COPY src/ src/

# Install the project itself
RUN uv pip install --system --no-cache .

# Default environment variables
ENV PIXOO_REST_HOST=0.0.0.0
ENV PIXOO_REST_PORT=5000
ENV PIXOO_HOST=Pixoo64

EXPOSE 5000

# Health check for FastAPI
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl --fail --silent http://localhost:${PIXOO_REST_PORT}/health || exit 1

# Run using uvicorn (FastAPI's ASGI server)
# Use shell form to allow environment variable expansion
CMD uvicorn pixoo_rest.app:app --host ${PIXOO_REST_HOST} --port ${PIXOO_REST_PORT}
