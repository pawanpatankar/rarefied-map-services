# ============================
# 1) BUILDER STAGE
# ============================
FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install build dependencies (only in this stage)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies into a temporary directory
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt


# ============================
# 2) FINAL RUNTIME STAGE
# ============================
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install only the built packages from builder stage
COPY --from=builder /install /usr/local

# Copy the actual application code
COPY . .

# Environment variables for Django superuser creation
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_PASSWORD=admin123
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com

EXPOSE 8000

# Run migrations, superuser, and start server
CMD ["sh", "-c", "python manage.py migrate && \
    python manage.py createsuperuser --noinput || true && \
    python manage.py runserver 0.0.0.0:8000"]

