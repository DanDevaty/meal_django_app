FROM python:3.11-slim

WORKDIR /app2

COPY app2/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app2/ .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


