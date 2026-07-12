from dataclasses import dataclass
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from src.RecordLifecycle.domain.ValueObjects.RecordTitle import RecordTitle
from src.RecordLifecycle.domain.ValueObjects.VideogameDescription import VideogameDescription
from src.RecordLifecycle.domain.ValueObjects.VideogamePlaytime import VideogamePlaytime
from src.RecordLifecycle.domain.ValueObjects.VideogameRating import VideogameRating 
from src.RecordLifecycle.domain.ValueObjects.CreationDate import CreationDate

@dataclass(frozen=True)
class UpdateVideogameRecordCommand: 
    id: RecordId
    author_id: AuthorId
    title: RecordTitle
    description: VideogameDescription
    playtime: VideogamePlaytime
    rating: VideogameRating 
    date: CreationDate