FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements-docker.txt

CMD ["uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "8000"]
