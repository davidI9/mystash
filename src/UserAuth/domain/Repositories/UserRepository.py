from abc import ABC, abstractmethod
from src.UserAuth.domain.ValueObjects import GoogleId, UserId, UserName
from ..Entities.User import User

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def find_by_id(self, user_id: UserId) -> User | None:
        pass

    @abstractmethod
    def find_by_username(self, username: UserName) -> User | None:
        pass

    @abstractmethod
    def find_by_google_id(self, google_id: GoogleId) -> User | None:
        pass
    