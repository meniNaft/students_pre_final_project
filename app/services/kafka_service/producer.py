import json
import os
from kafka import KafkaProducer


def producer_send_message(topic: str, value, key: str, require_flush: bool = False):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(
        topic,
        value=value,
        key=key.encode('utf-8')
    )

    if require_flush:
        producer.flush()
