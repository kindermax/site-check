from typing import Optional

from kafka import KafkaProducer


def create_kafka_producer(
    bootstrap_servers: str,
    ca_path: Optional[str],
    key_path: Optional[str],
    cert_path: Optional[str],
) -> KafkaProducer:
    with_ssl = all([ca_path, key_path, cert_path])

    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        security_protocol="SSL" if with_ssl else "PLAINTEXT",
        ssl_cafile=ca_path,
        ssl_certfile=cert_path,
        ssl_keyfile=key_path,
    )
    return producer
