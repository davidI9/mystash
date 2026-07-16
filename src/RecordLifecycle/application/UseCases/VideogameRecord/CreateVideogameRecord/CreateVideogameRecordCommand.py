from dataclasses import dataclass, field
from src.RecordLifecycle.domain.ValueObjects import CreationDate, RecordId, AuthorId, RecordTitle, VideogameDescription, VideogamePlaytime, VideogameRating

@dataclass(frozen=True)
class CreateVideogameRecordCommand:
    author: AuthorId
    game_title: RecordTitle
    date: CreationDate
    description: VideogameDescription
    rating: VideogameRating
    playtime: VideogamePlaytime
    id: RecordId