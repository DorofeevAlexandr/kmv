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


class Counter_line():
    def __init__(self) -> None:
        self.name = ''
        self.port = 0
        self.adr = 16
        self.k = 1
        self.no_connection_counter = False
        self.indikator_value = 0
        self.legth = 0
        self.speed_line = 0
        self.description = ''
        self.created_dt = 0
        self.updated_dt = 0