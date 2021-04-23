import sys
import logging

from checker.checker import Checker
from checker.config import (
    parse_config,
    Config,
)
from checker.exception import CheckerError
from checker.kafka import create_kafka_producer
from checker.parser import create_parser

log = logging.getLogger(__name__)


def setup_logging():
    logging.basicConfig(level=logging.INFO)


def run(config: Config):
    log.info(f'Running checker with config {config}')
    kafka_producer = create_kafka_producer(
        config.kafka_bootstrap,
        config.kafka_ca_path,
        config.kafka_key_path,
        config.kafka_cert_path
    )
    checker = Checker(config, kafka_producer)
    checker.run()


try:
    setup_logging()
    parser = create_parser()
    config = parse_config(parser)
    run(config)
except KeyboardInterrupt:
    log.info('Stopping checker ...')
except CheckerError as e:
    log.error(f'Failed to run checker: {e}')
    sys.exit(1)
except Exception as e:
    log.exception('Unexpected exception')
    sys.exit(1)

