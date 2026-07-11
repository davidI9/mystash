from dataclasses import dataclass
from src.RecordLifecycle.domain.ValueObjects import AuthorId

@dataclass
class GetUserVideogameRecordsCommand:
    author_id: AuthorId