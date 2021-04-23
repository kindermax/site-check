from argparse import ArgumentParser
from dataclasses import dataclass


@dataclass
class Config:
    kafka_bootstrap: str
    kafka_topic: str
    postgres_uri: str


def parse_config(parser: ArgumentParser) -> Config:
    args = parser.parse_args()

    return Config(
        kafka_bootstrap=args.kafka_bootstrap,
        kafka_topic=args.kafka_topic,
        postgres_uri=args.postgres_uri,
    )
