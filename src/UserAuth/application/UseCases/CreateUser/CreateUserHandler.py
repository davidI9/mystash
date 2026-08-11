from src.UserAuth.application.UseCases.CreateUser.CreateUserCommand import CreateUserCommand
from src.UserAuth.domain.Entities.User import User
from src.UserAuth.domain.Repositories.UserRepository import UserRepository
from src.UserAuth.domain.ValueObjects.UserName import UserName
from src.UserAuth.domain.ValueObjects.GoogleId import GoogleId
from src.UserAuth.domain.ValueObjects.Email import Email
from src.UserAuth.domain.ValueObjects.AvatarUrl import AvatarUrl
from src.shared.application.IEventBus import IEventBus

class CreateUserHandler:
    def __init__(self, user_repository: UserRepository, event_bus: IEventBus):
        self.user_repository = user_repository
        self.event_bus = event_bus

    def handle(self, command: CreateUserCommand) -> str:
        email_vo = Email(command.email)
        google_id_vo = GoogleId(command.google_id)
        avatar_url_vo = AvatarUrl(command.avatar_url) if command.avatar_url else None
        
        if self.user_repository.find_by_google_id(google_id_vo):
            raise ValueError("User already exists")

        user = User.create(
            email=email_vo,
            google_id=google_id_vo,
            avatar_url=avatar_url_vo
        )
        
        if command.username:
            user.update_username(UserName(command.username))
        else:
            short_id = str(user.id.value).replace("-", "")[:15]
            user.update_username(UserName(f'user_{short_id}'))

        self.user_repository.save(user)
        
        events = user.pull_domain_events()
        self.event_bus.publish(events)
            
        return str(user.id.value)