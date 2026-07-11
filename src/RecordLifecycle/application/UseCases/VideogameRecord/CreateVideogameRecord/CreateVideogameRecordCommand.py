from dataclasses import dataclass, field
from src.RecordLifecycle.domain.ValueObjects import CreationDate, RecordId, AuthorId, RecordTitle, VideogameDescription, VideogamePlaytime, VideogameRating

@dataclass
class CreateVideogameRecordCommand:
    author: AuthorId
    title: RecordTitle
    date: CreationDate
    description: VideogameDescription
    playtime: VideogamePlaytime
    rating: VideogameRating
    id: RecordId