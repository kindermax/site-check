import sys
from dataclasses import dataclass

from checker import Checker
from checker.exception import CheckerError
from checker.validator import validate_url


@dataclass
class Args:
    site: str


def parse_args(args: list) -> Args:
    if len(args) != 2:
        print('Provide <site> argument')
        sys.exit(1)

    site = sys.argv[1]

    validate_url(site)

    return Args(
        site=site
    )


def run(args: Args):
    checker = Checker(args.site)
    checker.run()


try:
    args = parse_args(sys.argv)
    run(args)
except KeyboardInterrupt:
    print('Stopping checker ...')
except CheckerError as e:
    print(f'Failed to run checker: {e}')
    sys.exit(1)
except Exception as e:
    print(f'Unexpected exception: {e}')
    sys.exit(1)

