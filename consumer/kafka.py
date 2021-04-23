from kafka import KafkaConsumer


def create_kafka_consumer(
    bootstrap_servers: str,
    topic: str,
) -> KafkaConsumer:
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
    )
    return consumer
