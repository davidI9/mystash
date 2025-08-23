from dataclasses import dataclass, field
from src.RecordLifecycle.domain.ValueObjects import RecordId, AuthorId

@dataclass
class CreateVideogameRecordCommand:
    author: AuthorId
    title: str
    date: str
    description: str
    playtime: int
    rating: float | int
    id: 'RecordId' = field(default_factory=lambda: RecordId())