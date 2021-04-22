import time
from urllib.request import urlopen
from dataclasses import dataclass


@dataclass
class Check:
    # in milliseconds
    response_time: float
    http_status_code: int


class Checker:
    def __init__(
        self,
        url: str,
        interval: int,
    ):
        self.url = url
        self.interval = interval

    def run(self):
        while True:
            check = self._make_request()
            print('check', check)
            time.sleep(self.interval)

    def _make_request(self) -> Check:
        """Make a request to site
        TODO handle timeout
        """
        start = time.monotonic()
        resp = urlopen(self.url)
        took = round((time.monotonic() - start) * 1000)

        return Check(
            response_time=took,
            http_status_code=resp.status
        )
