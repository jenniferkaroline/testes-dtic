FROM python:3.11.9

WORKDIR /app

COPY . /app

COPY start.sh /app

RUN pip install --no-cache-dir -r dependencias.txt

ENV POSTGRES_PORT=5433

CMD ["python", "app/app.py"]
