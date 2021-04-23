from argparse import ArgumentParser
from dataclasses import dataclass

from common.config import KafkaConfig


@dataclass
class Config(KafkaConfig):
    postgres_uri: str


def parse_config(parser: ArgumentParser) -> Config:
    args = parser.parse_args()

    return Config(
        kafka_bootstrap=args.kafka_bootstrap,
        kafka_topic=args.kafka_topic,
        kafka_ca_path=args.kafka_ca_path,
        kafka_key_path=args.kafka_key_path,
        kafka_cert_path=args.kafka_cert_path,
        postgres_uri=args.postgres_uri,
    )
