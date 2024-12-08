FROM python:3.12-slim-bullseye

# Set the working directory
WORKDIR /app

# Run the update command to update the package list
RUN apt update && \
    apt upgrade -y && \
    apt clean && \
    apt install --no-install-recommends

# Create virtual environment
ENV VIRTUAL_ENV=/app/venv
RUN python3 -m venv --system-site-packages $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy the pyproject.toml file to the working directory
COPY pyproject.toml ./
