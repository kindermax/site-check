import json

from dataclasses import dataclass, asdict


@dataclass
class Check:
    # in milliseconds
    response_time: int
    status_code: int
    url: str

    def serialize(self) -> bytes:
        return json.dumps(asdict(self)).encode('utf-8')

    @staticmethod
    def deserialize(raw_check: bytes) -> 'Check':
        data = json.loads(raw_check.decode('utf-8'))
        return Check(**data)
