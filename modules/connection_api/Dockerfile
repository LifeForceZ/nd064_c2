FROM python:3.7-slim

WORKDIR .

RUN apt get-install -y gcc musl-dev linux-headers geos libc-dev postgresql-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]