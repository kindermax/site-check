from argparse import ArgumentParser
from dataclasses import dataclass

from checker.validator import validate_url

DEFAULT_INTERVAL = 10  # in seconds


@dataclass
class Config:
    site: str
    interval: int
    kafka_bootstrap: str
    kafka_topic: str


def parse_config(parser: ArgumentParser) -> Config:
    args = parser.parse_args()
    validate_url(args.site)

    return Config(
        site=args.site,
        interval=args.interval or DEFAULT_INTERVAL,
        kafka_bootstrap=args.kafka_bootstrap,
        kafka_topic=args.kafka_topic,
    )
