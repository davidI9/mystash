ARG CODE_VERSION=latest

FROM python:3.12-slim-trixie as base
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . .

RUN uv sync --locked

EXPOSE 8000

FROM base as startup

CMD ["uv", "run", "fastapi", "run", "src/RecordLifecycle/infrastructure/Controllers/VideogameRecordApi.py", "--port", "8000"]