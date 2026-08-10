from dataclasses import dataclass
from typing import Optional

@dataclass
class CreateUserCommand:
    email: str
    google_id: str
    username: Optional[str] = None
    avatar_url: Optional[str] = None