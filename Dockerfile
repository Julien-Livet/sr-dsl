FROM ubuntu:26.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-pytest \
    python3-venv \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . sr-dsl
WORKDIR /app/sr-dsl
RUN python3 -m venv .venv && . .venv/bin/activate && python -m pip install -r requirements.txt

ENTRYPOINT ["/bin/bash"]

