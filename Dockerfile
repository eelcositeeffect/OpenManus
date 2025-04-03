# Stage 1: Node frontend (optional, if needed)
FROM node:20-alpine AS frontend

WORKDIR /app/frontend

COPY package*.json ./
RUN npm install
COPY . .

# Stage 2: Python backend
FROM python:3.11-slim AS backend

WORKDIR /app

RUN apt-get update && apt-get install -y curl && \
    pip install playwright && \
    playwright install

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code (adjust this depending on actual structure)
COPY . .

# Expose port if needed by backend
EXPOSE 8055

# Start Python ASGI app (adjust 'main:app' if needed)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8055"]