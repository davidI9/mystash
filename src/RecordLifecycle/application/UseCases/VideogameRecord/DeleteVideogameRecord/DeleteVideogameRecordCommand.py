from dataclasses import dataclass
from src.RecordLifecycle.domain.ValueObjects import RecordId

@dataclass(frozen=True)
class DeleteVideogameRecordCommand:
    id: RecordId