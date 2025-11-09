FROM python:3.12-bookworm

ENV PYTHONUNBUFFERED=1

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apt-get update && \
    apt-get install --yes --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/app

# Copy project files
COPY pyproject.toml .
COPY README.md .

# Install dependencies using uv
RUN uv pip install --system --no-cache -r pyproject.toml

# Copy application source code
COPY src/ src/

HEALTHCHECK --interval=5m --timeout=3s \
    CMD curl --fail --silent http://localhost:5000/${SCRIPT_NAME}/health || exit 1

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "--pythonpath", "src", "pixoo_rest.main:app" ]
