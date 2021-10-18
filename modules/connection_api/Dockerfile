FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc g++ musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements_rest.txt requirements_grpc.txt requirements_kafka.txt ./
RUN pip install -r requirements.txt
RUN pip install -r requirements_rest.txt
# RUN pip install -r requirements_grpc.txt

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]