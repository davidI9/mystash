from dataclasses import dataclass
from src.shared.domain.Aggregate import Aggregate
from typing import Optional
from datetime import datetime, timezone
from src.UserAuth.domain.ValueObjects.UserId import UserId
from src.UserAuth.domain.ValueObjects.Email import Email
from src.UserAuth.domain.ValueObjects.UserName import UserName
from src.UserAuth.domain.ValueObjects.AvatarUrl import AvatarUrl
from src.UserAuth.domain.Events.UserCreated import UserCreated
from src.UserAuth.domain.Events.UserUpdated import UserUpdated
from src.UserAuth.domain.ValueObjects.GoogleId import GoogleId

@dataclass
class User(Aggregate):
    id: UserId
    email: Email
    google_id: GoogleId
    created_at: datetime
    updated_at: datetime
    username: Optional[UserName] = None
    avatar_url: Optional[AvatarUrl] = None

    @classmethod
    def create(cls, email: Email, google_id: GoogleId, avatar_url: Optional[AvatarUrl] = None) -> 'User':
        user_id = UserId.generate()
        now = datetime.now(timezone.utc)
        user = cls(
            id=user_id,
            email=email,
            google_id=google_id,
            created_at=now,
            updated_at=now,
            avatar_url=avatar_url
        )
        
        user._record_event(UserCreated(user_id=user_id.value, email=email.value))
        
        return user
        
    def update_email(self, new_email: Email):
        self.email = new_email
        self.updated_at = datetime.now(timezone.utc)
        
        self._record_event(UserUpdated(user_id=self.id.value))
        
    def update_avatar(self, new_avatar_url: AvatarUrl):
        self.avatar_url = new_avatar_url
        self.updated_at = datetime.now(timezone.utc)
        
        self._record_event(UserUpdated(user_id=self.id.value))
    
    def update_username(self, new_username: UserName):
        self.username = new_username
        self.updated_at = datetime.now(timezone.utc)
        
        self._record_event(UserUpdated(user_id=self.id.value))