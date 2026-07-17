from dataclasses import dataclass
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId

@dataclass(frozen=True)
class GetSongRecordCommand:
    record_id: RecordId