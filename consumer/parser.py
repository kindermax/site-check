from argparse import ArgumentParser

from common.parser import add_kafka_options


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(description='Consume site checks')

    parser.add_argument(
        '--postgres-uri',
        dest='postgres_uri',
        type=str,
        help='Specify postgres database (postgres://user:pass@host:port/db)',
        required=True,
    )

    add_kafka_options(parser)

    return parser

