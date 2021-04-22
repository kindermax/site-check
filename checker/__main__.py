import sys

from dataclasses import dataclass
from argparse import (
    ArgumentParser,
)

from checker import Checker
from checker.exception import CheckerError
from checker.validator import validate_url


DEFAULT_INTERVAL = 10  # in seconds


@dataclass
class Args:
    site: str
    interval: int


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

    return parser


def parse_args(parser: ArgumentParser) -> Args:
    args = parser.parse_args()
    validate_url(args.site)

    return Args(
        site=args.site,
        interval=args.interval or DEFAULT_INTERVAL,
    )


def run(args: Args):
    checker = Checker(args.site, args.interval)
    print(f'Running checker on {args.site} with interval {args.interval}')
    checker.run()

try:
    parser = create_parser()
    args = parse_args(parser)
    run(args)
except KeyboardInterrupt:
    print('Stopping checker ...')
except CheckerError as e:
    print(f'Failed to run checker: {e}')
    sys.exit(1)
except Exception as e:
    print(f'Unexpected exception: {e}')
    sys.exit(1)

