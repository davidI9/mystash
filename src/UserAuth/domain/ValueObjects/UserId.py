from dataclasses import dataclass
from uuid import uuid4, UUID

@dataclass(frozen=True)
class UserId:
    value: UUID
    
    def __post_init__(self):
        if not self.value:
            raise ValueError("UserId cannot be empty.")
        if not isinstance(self.value, UUID):
            raise ValueError("UserId must be a UUID.")
    
    @classmethod
    def generate(cls) -> 'UserId':
        return cls(value=uuid4())