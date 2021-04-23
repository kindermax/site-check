from dataclasses import dataclass
from typing import Optional


@dataclass
class KafkaConfig:
    kafka_bootstrap: str
    kafka_topic: str
    kafka_ca_path: Optional[str]
    kafka_key_path: Optional[str]
    kafka_cert_path: Optional[str]

