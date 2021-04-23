import logging

from typing import (
    Any,
)

import psycopg2


DB = Any

log = logging.getLogger(__name__)


def create_db_client(
    uri: str,
) -> DB:
    conn = psycopg2.connect(uri)
    log.info('Connected to db %s', uri)
    return conn
