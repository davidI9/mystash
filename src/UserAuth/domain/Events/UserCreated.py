from dataclasses import dataclass
from src.shared.domain.DomainEvent import DomainEvent

@dataclass(kw_only=True)
class UserCreated(DomainEvent):
    user_id: str
    email: str