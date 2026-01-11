FROM python:3-slim

# Install git
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.d/entrypoint.sh
RUN chmod +x /entrypoint.d/entrypoint.sh

ENTRYPOINT ["/bin/bash", "/entrypoint.d/entrypoint.sh"]
