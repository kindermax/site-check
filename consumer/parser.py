from argparse import ArgumentParser


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(description='Consume site checks')

    # TODO may be many
    # type list int
    parser.add_argument(
        '--kafka-bootstrap',
        dest='kafka_bootstrap',
        type=str,
        help='Specify kafka bootstrap servers',
        required=True,
    )

    parser.add_argument(
        '--kafka-topic',
        dest='kafka_topic',
        type=str,
        help='Specify kafka topic',
        required=True,
    )

    parser.add_argument(
        '--postgres-uri',
        dest='postgres_uri',
        type=str,
        help='Specify postgres database (postgres://user:pass@host:port/db)',
        required=True,
    )

    return parser

