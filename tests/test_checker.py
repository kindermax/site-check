from checker import Checker


def test_checker_smoke():
    checker = Checker('https://google.com')

    assert checker.url == 'https://google.com'
