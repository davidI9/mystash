from dataclasses import dataclass
from src.RecordLifecycle.domain.ValueObjects.AuthorId import RecordId

@dataclass(frozen=True)
class DeleteSongRecordCommand:
    record_id: RecordId