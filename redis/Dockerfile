FROM python:3.13-slim

WORKDIR /app

# Copy script into the container
COPY insert.py .

# Install redis library
RUN pip install redis

# Run the script
CMD ["python", "insert.py"]
