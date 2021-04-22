import unittest

from checker.validator import (
    ErrInvalidUrl,
    validate_url,
)


class TestUrlValidator(unittest.TestCase):
    def test_validate_url_failed(self):
        with self.assertRaises(ErrInvalidUrl) as err:
            validate_url("http://")

        with self.assertRaises(ErrInvalidUrl) as err:
            validate_url("http://goo")

    def test_validate_url_ok(self):
        validate_url("http://google.com")
