FROM python:3.10-slim

# Probably should do update/upgrade for any CVEs

WORKDIR /app

# Set up requirements
COPY requirements.txt requirements.txt
# hadolint ignore=DL3013
RUN python3 -m pip install pip --upgrade --no-cache-dir && \
    python3 -m pip install -r requirements.txt --no-cache-dir

# Copy in code
COPY ./src/musort.py musort.py

# Usage: docker run -rm -n musort -it musort --help
ENTRYPOINT ["python3", "/app/musort.py"]