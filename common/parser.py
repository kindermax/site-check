from argparse import ArgumentParser


def add_kafka_options(parser: ArgumentParser):
    parser.add_argument(
        '--kafka-bootstrap',
        dest='kafka_bootstrap',
        type=str,
        help='Specify kafka bootstrap servers',
        required=True,
    )
    parser.add_argument(
        '--kafka-topic',
        dest='kafka_topic',
        type=str,
        help='Specify kafka topic',
        required=True,
    )
    parser.add_argument(
        '--kafka-ca-path',
        dest='kafka_ca_path',
        help="Specify CA certificate path",
        required=True
    )
    parser.add_argument(
        '--kafka-key-path',
        dest='kafka_key_path',
        help="Specify Kafka Access Key path",
        required=True
    )
    parser.add_argument(
        '--kafka-cert-path',
        dest='kafka_cert_path',
        help="Specify Kafka Certificate Key path",
        required=True
    )
