# src/contexts/shared/domain/domain_event.py
from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid

@dataclass
class DomainEvent:
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    occurred_on: datetime = field(default_factory=lambda: datetime.now(timezone.utc))