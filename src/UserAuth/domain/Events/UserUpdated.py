from src.shared.domain.DomainEvent import DomainEvent
from src.UserAuth.domain.ValueObjects.UserId import UserId
from dataclasses import dataclass

@dataclass
class UserUpdated(DomainEvent):
    user_id: UserId