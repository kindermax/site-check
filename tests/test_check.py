from common.check import Check


def test_check_serialize():
    check = Check(
        response_time=100,
        status_code=201,
        url='http://google.com'
    )
    assert check.serialize() == b'{"response_time": 100, "status_code": 201, "url": "http://google.com"}'


def test_check_deserialize():
    expected = Check(
        response_time=100,
        status_code=201,
        url='http://google.com'
    )
    got = Check.deserialize(b'{"response_time": 100, "status_code": 201, "url": "http://google.com"}')
    assert expected == got
