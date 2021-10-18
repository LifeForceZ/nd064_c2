from kafka import KafkaConsumer

import json

import logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")


TOPIC_NAME = "visits"
KAFKA_SERVER = "localhost:9092"

consumer = KafkaConsumer(TOPIC_NAME)

for message in consumer:
    print(message)