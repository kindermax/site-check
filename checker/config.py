from argparse import ArgumentParser
from dataclasses import dataclass

from checker.validator import (
    validate_url,
    normalize_url,
)
from common.config import KafkaConfig

DEFAULT_INTERVAL = 10  # in seconds


@dataclass
class Config(KafkaConfig):
    # normalized url using https://github.com/niksite/url-normalize
    site: str
    interval: int


def parse_config(parser: ArgumentParser) -> Config:
    args = parser.parse_args()
    validate_url(args.site)

    return Config(
        site=normalize_url(args.site),
        interval=args.interval or DEFAULT_INTERVAL,
        kafka_bootstrap=args.kafka_bootstrap,
        kafka_topic=args.kafka_topic,
        kafka_ca_path=args.kafka_ca_path,
        kafka_key_path=args.kafka_key_path,
        kafka_cert_path=args.kafka_cert_path,
    )
