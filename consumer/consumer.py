import logging

from kafka import KafkaConsumer

from common.check import Check
from consumer.config import Config
from consumer.db import DB


log = logging.getLogger(__name__)


def insert_check(db: DB, check: Check) -> None:
    cur = db.cursor()
    insert_stmt = """
    INSERT INTO checks (url, response_time, status_code)
    VALUES (%s, %s, %s)
    """

    cur.execute(insert_stmt, (
        check.url,
        check.response_time,
        check.status_code
    ))

    db.commit()
    cur.close()


class Consumer:
    def __init__(
        self,
        config: Config,
        consumer: KafkaConsumer,
        db: DB
    ):
        self.consumer = consumer
        self.topic = config.kafka_topic
        self.db = db

    def run(self):
        for msg in self.consumer:
            try:
                self.handle_message(msg.value)
            except Exception:
                log.exception('Failed to handle message from kafka: %s', msg)

    def handle_message(self, raw_msg: bytes) -> None:
        check = Check.deserialize(raw_msg)
        insert_check(self.db, check)
