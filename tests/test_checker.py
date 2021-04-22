from checker import Checker


def test_checker_smoke():
    checker = Checker('https://google.com', 10)

    assert checker.url == 'https://google.com'
