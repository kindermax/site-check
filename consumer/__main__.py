import sys
import logging

from consumer.consumer import Consumer
from consumer.config import (
    parse_config,
    Config,
)
from consumer.db import create_db_client
from consumer.exception import ConsumerError
from consumer.kafka import create_kafka_consumer
from consumer.parser import create_parser
from common.logging import setup_logging

log = logging.getLogger(__name__)


def run(config: Config):
    log.info(f'Running consumer with config {config}')
    kafka_consumer = create_kafka_consumer(
        config.kafka_bootstrap,
        config.kafka_topic,
        config.kafka_ca_path,
        config.kafka_key_path,
        config.kafka_cert_path
    )
    db = create_db_client(config.postgres_uri)
    consumer = Consumer(config, kafka_consumer, db)
    consumer.run()


try:
    setup_logging()
    parser = create_parser()
    config = parse_config(parser)
    run(config)
except KeyboardInterrupt:
    log.info('Stopping consumer ...')
except ConsumerError as e:
    log.error(f'Failed to run consumer: {e}')
    sys.exit(1)
except Exception as e:
    log.exception('Unexpected exception')
    sys.exit(1)

