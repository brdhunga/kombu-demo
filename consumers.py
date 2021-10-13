import kombu
from loguru import logger


from connection import kombu_conn, test_queue


kombu_conn.connect()


def callback(body, message):
    logger.info("Received message")
    print(body, message)
    message.ack()


with kombu_conn as conn:
    with conn.default_channel as channel:
        consumer = kombu.Consumer(
            conn, [test_queue], accept=['json']
        )
        consumer.register_callback(callback)
        with consumer:
            conn.drain_events(timeout=5)
