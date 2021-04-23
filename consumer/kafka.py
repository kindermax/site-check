from typing import Optional

from kafka import KafkaConsumer


def create_kafka_consumer(
    bootstrap_servers: str,
    topic: str,
    ca_path: Optional[str],
    key_path: Optional[str],
    cert_path: Optional[str],
) -> KafkaConsumer:
    with_ssl = all([ca_path, key_path, cert_path])
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        security_protocol="SSL" if with_ssl else "PLAINTEXT",
        ssl_cafile=ca_path,
        ssl_certfile=cert_path,
        ssl_keyfile=key_path,
    )
    return consumer
