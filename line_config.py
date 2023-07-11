import uuid
from dataclasses import dataclass, field


@dataclass()
class Line:
    name: str
    adr: int
    k: float
    no_connection_counter: bool
    legth: float = field(default=0.0)
    description: str
    creation_date: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)

