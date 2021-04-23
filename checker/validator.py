from url_normalize import url_normalize
from validators import url

from checker.exception import CheckerError


class ErrInvalidUrl(CheckerError):
    pass


def validate_url(raw_url: str) -> None:
    if not url(raw_url):
        raise ErrInvalidUrl(f'Invalid url provided: {raw_url}')


def normalize_url(raw_url: str) -> str:
    return url_normalize(raw_url)
