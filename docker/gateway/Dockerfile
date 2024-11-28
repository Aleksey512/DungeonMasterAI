FROM python:3.12.1-slim-bullseye

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        python3-dev \
        gcc \
        musl-dev \
        git \
        curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY services.gateway/main.pex .

CMD ["/app/__main__.py"]
