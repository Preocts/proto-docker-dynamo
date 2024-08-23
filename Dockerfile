FROM python:3.12-slim-bookworm AS builder

ENV LANG=C.UTF-8

WORKDIR /app
COPY . .

RUN python -m pip install --target artifact .

FROM python:3.12-slim-bookworm AS app

RUN useradd --user-group --system --no-create-home --no-log-init app-user
WORKDIR /app
COPY --from=builder --chown=app-user:app-user /app/artifact /app

USER app-user

CMD ["python", "-m", "flask", "--app", "pdd.app:app", "run", "-h", "0.0.0.0", "-p", "9090", "--with-threads"]
