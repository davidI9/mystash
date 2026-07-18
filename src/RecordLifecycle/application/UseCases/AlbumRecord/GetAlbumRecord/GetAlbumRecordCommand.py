from dataclasses import dataclass
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId

@dataclass(frozen=True)
class GetAlbumRecordCommand:
    record_id: RecordId