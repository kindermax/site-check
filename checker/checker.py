import time

from urllib.request import urlopen

from kafka import KafkaProducer

from checker.config import Config
from common.check import Check


class Checker:
    def __init__(
        self,
        config: Config,
        producer: KafkaProducer
    ):
        self.url = config.site
        self.interval = config.interval
        self.producer = producer
        self.topic = config.kafka_topic

    def run(self, once: bool = False):
        while True:
            check = self._make_request()
            self.send_check_event(check)
            if once:
                break
            time.sleep(self.interval)

    def send_check_event(self, event: Check):
        self.producer.send(self.topic, event.serialize())

    def _make_request(self) -> Check:
        """Make a request to site
        TODO handle timeout
        """
        start = time.monotonic()
        resp = urlopen(self.url)
        took = round((time.monotonic() - start) * 1000)

        return Check(
            response_time=took,
            status_code=resp.status,
            url=self.url,
        )
