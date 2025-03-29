# Use Python base image for easy pip usage
FROM python:3.10-slim

# Install Tor and other dependencies
RUN apt-get update && \
    apt-get install -y tor && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install onionshare-cli via pip
RUN pip install --no-cache-dir onionshare-cli

# Create site directory
WORKDIR /site
COPY index.html /site/index.html

# Expose port (optional for debugging, not needed for Tor)
EXPOSE 17600

# Entrypoint and default command
ENTRYPOINT ["onionshare-cli"]
CMD ["--web", "/site", "--use-onion-service", "v3", "--disable-auto-open", "--disable-text-clip", "--disable-auto-start", "--no-log"]
