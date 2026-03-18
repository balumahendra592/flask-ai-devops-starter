# --- Build Stage ---
FROM python:3.12-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# --- Runtime Stage ---
FROM python:3.12-slim

WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .

# Don't run as root
RUN useradd -m appuser
USER appuser

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
