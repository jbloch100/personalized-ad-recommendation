# Use Python 3.11 slim as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy source and test code
COPY src/ ./src/
COPY tests/ ./tests/

# Set environment variable
ENV PYTHONPATH=/app

# Command to run the app
CMD ["python", "src/main.py"]