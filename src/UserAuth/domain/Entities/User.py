from dataclasses import dataclass, classmethod
from src.shared.domain.Aggregate import Aggregate
from typing import Optional
from datetime import datetime
from src.UserAuth.domain.ValueObjects.UserId import UserId
from src.UserAuth.domain.ValueObjects.Email import Email
from src.UserAuth.domain.ValueObjects.UserName import UserName
from src.UserAuth.domain.ValueObjects.AvatarUrl import AvatarUrl
from src.UserAuth.domain.Events.UserCreated import UserCreated

@dataclass
class User(Aggregate):
    id: UserId
    email: Email
    username: UserName
    google_id: str
    created_at: datetime
    updated_at: datetime
    avatar_url: Optional[AvatarUrl] = None

    @classmethod
    def create(cls, email: Email, username: UserName, google_id: str, avatar_url: Optional[AvatarUrl] = None):
        user_id = UserId.generate()
        now = datetime.now()
        user = cls(
            id=user_id,
            email=email,
            username=username,
            google_id=google_id,
            created_at=now,
            updated_at=now,
            avatar_url=avatar_url
        )
        
        user._record_event(UserCreated(user_id=user_id, email=email, username=username))
        
        return user
        