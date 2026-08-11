from src.shared.domain.DomainEvent import DomainEvent
from dataclasses import dataclass

@dataclass(kw_only=True)
class UserUpdated(DomainEvent):
    user_id: str