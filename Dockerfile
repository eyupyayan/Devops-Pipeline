FROM python:3.12-slim

# 1) Basic runtime settings
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 2) Create non-root user (beginner-friendly security hygiene)
RUN useradd -m appuser

WORKDIR /app

# 3) Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) Copy application code
COPY app ./app

# 5) Switch to non-root
USER appuser

EXPOSE 8000

# 6) Start the web server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]