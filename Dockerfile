# Stage 1: Builder (compila e installa dipendenze)
FROM python:3.13-slim as builder

WORKDIR /app

# Installa dipendenze di sistema per build
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements e installa dipendenze Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Stage 2: Production (immagine finale leggera)
FROM python:3.13-slim

# Crea utente non-root per sicurezza
RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

# Copia dipendenze Python dallo stage builder
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copia codice dell'applicazione
COPY --chown=appuser:appuser . .

# Passa a utente non-root
USER appuser

# Esponi porta FastAPI
EXPOSE 8000

# Comando per avviare l'applicazione
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
