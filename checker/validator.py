from validators import url

from checker.exception import CheckerError


class ErrInvalidUrl(CheckerError):
    pass


def validate_url(raw_url: str) -> None:
    if not url(raw_url):
        raise ErrInvalidUrl(f'Invalid url provided: {raw_url}')

