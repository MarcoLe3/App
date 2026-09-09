# Start with Python installed.
FROM python:3.14.4-slim-bookworm

# Run the following commands inside /app.
WORKDIR /app

# Show Python logs immediately in Docker.
ENV PYTHONUNBUFFERED=1

# Install dependencies before copying code so Docker can cache this step.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server code into the image.
COPY . .

# Match the API port in docker-compose.yml.
EXPOSE 8000

# Start the app defined in main.py, accessible outside the container.
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
