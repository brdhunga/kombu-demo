import kombu
from loguru import logger
import json

from connection import kombu_conn, test_queue




kombu_conn.connect()

with kombu_conn as conn:
    with conn.default_channel as channel:
        producer = kombu.Producer(channel)
        logger.info("Sending message..")
        producer.publish(
                    json.dumps(({"hello": "world"})).encode(),
                    retry=True,
                    exchange=test_queue.exchange,
                    routing_key=test_queue.routing_key,
                    declare=[test_queue],
                    content_type="json",
                    body_encoding="utf-8",
                    compression=False,
                    serializer='my_json',
                    dfdfd="dfdf"
        )
