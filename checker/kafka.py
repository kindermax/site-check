from kafka import KafkaProducer


def create_kafka_producer(
    bootstrap_servers: str,
) -> KafkaProducer:
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    return producer
