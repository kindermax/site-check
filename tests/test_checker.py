from unittest.mock import (
    MagicMock,
    patch,
    Mock,
)

from checker.checker import Checker
from checker.config import Config
from common.check import Check


def test_checker_smoke():
    config = Config(
        site='https://google.com',
        interval=10,
        kafka_bootstrap='localhost:9002',
        kafka_topic='checks',
        kafka_ca_path='./',
        kafka_key_path='./',
        kafka_cert_path='./'
    )

    producer = MagicMock()
    checker = Checker(config, producer)

    assert checker.url == 'https://google.com'


def test_checker_send_event():
    config = Config(
        site='https://google.com',
        interval=10,
        kafka_bootstrap='localhost:9002',
        kafka_topic='checks',
        kafka_ca_path='./',
        kafka_key_path='./',
        kafka_cert_path='./'
    )

    producer = Mock()
    checker = Checker(config, producer)

    check = Check(
        response_time=100,
        status_code=201,
        url='http://google.com'
    )
    with patch.object(Checker, '_make_request', return_value=check):
        checker.run(once=True)

    producer.send.assert_called_once_with(
        'checks', b'{"response_time": 100, "status_code": 201, "url": "http://google.com"}'
    )
