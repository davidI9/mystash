from dataclasses import dataclass, field
from DomainEvent import DomainEvent

@dataclass
class Aggregate:
    _domain_events: list[DomainEvent] = field(
        default_factory=list, init=False, repr=False, compare=False
    )

    def _record_event(self, event: DomainEvent) -> None:
        self._domain_events.append(event)

    def pull_domain_events(self) -> list[DomainEvent]:
        events = self._domain_events.copy()
        self._domain_events.clear()
        return events