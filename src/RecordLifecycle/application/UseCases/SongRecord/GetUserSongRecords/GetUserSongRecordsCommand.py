from dataclasses import dataclass
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId

@dataclass(frozen=True)
class GetUserSongRecordsCommand:
    author_id: AuthorId