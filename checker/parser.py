from argparse import ArgumentParser

from common.parser import add_kafka_options


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

    add_kafka_options(parser)

    return parser

