from dataclasses import dataclass
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId

@dataclass(frozen=True)
class DeleteSongRecordCommand:
    record_id: RecordId