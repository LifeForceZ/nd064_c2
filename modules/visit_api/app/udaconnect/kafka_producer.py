from kafka import KafkaProducer

import json

import logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")


TOPIC_NAME = "visits"
KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

message = {
    "person_id":1,
    "coordinate":"010100000097FDBAD39D925EC0D00A0C59DDC64240",
    "creation_time":"2020-07-07 10:37:06.000000"
}

producer.send(TOPIC_NAME, json.dumps(message))
producer.flush()