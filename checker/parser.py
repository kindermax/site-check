from argparse import ArgumentParser


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(description='Check site')
    parser.add_argument(
        'site',
        type=str,
        help='Specify site url to check',
    )

    parser.add_argument(
        '--interval',
        dest='interval',
        type=int,
        help='Specify interval (in seconds) to check',
        required=False,
    )

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

    return parser

