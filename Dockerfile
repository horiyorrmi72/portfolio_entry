FROM python:3.12-slim
WORKDIR /app

#insatlling system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*
    
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "portfolio_edits.wsgi:application", "--bind", "0.0.0.0:8000"]