from dataclasses import dataclass
from src.RecordLifecycle.domain.ValueObjects import AuthorId

@dataclass(frozen=True)
class GetUserVideogameRecordsCommand:
    author_id: AuthorId