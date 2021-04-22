from unittest.mock import (
    MagicMock,
    patch,
    Mock,
)

from checker.checker import (
    Checker,
    Check,
)
from checker.config import Config


def test_checker_smoke():
    config = Config(
        'https://google.com',
        10,
        'localhost:9002',
        'checks'
    )

    producer = MagicMock()
    checker = Checker(config, producer)

    assert checker.url == 'https://google.com'


def test_checker_send_event():
    config = Config(
        'https://google.com',
        10,
        'localhost:9002',
        'checks'
    )

    producer = Mock()
    checker = Checker(config, producer)

    check = Check(
        response_time=100,
        http_status_code=201,
    )
    with patch.object(Checker, '_make_request', return_value=check):
        checker.run(once=True)

    producer.send.assert_called_once_with(
        'checks', b'{"response_time": 100, "http_status_code": 201}'
    )
