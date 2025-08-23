from dataclasses import dataclass
from src.RecordLifecycle.domain.ValueObjects import RecordId

@dataclass
class GetVideogameRecordCommand:
    id: RecordId