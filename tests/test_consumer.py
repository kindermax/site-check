from unittest.mock import (
    Mock,
)

from common.check import Check
from consumer.consumer import Consumer
from consumer.config import Config


def test_consumer_handle_event():
    config = Config(
        kafka_bootstrap='localhost:9002',
        kafka_topic='checks',
        kafka_ca_path='./',
        kafka_key_path='./',
        kafka_cert_path='./',
        postgres_uri='postgres://user:pass@localhost:port/db'
    )

    check = Check(
        response_time=100,
        status_code=201,
        url='http://google.com'
    )

    event = Mock()
    event.value = check.serialize()

    kafka_consumer = [event]
    db = Mock()
    cursor = Mock()
    db.cursor = Mock(return_value=cursor)

    consumer = Consumer(config, kafka_consumer, db)  # type: ignore

    consumer.run()

    cursor.execute.assert_called()
