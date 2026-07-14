from src.RecordLifecycle.application.UseCases.VideogameRecord.CreateVideogameRecord.CreateVideogameRecordCommand import CreateVideogameRecordCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.CreateVideogameRecord.CreateVideogameRecordHandler import CreateVideogameRecordHandler
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from src.RecordLifecycle.domain.ValueObjects.RecordTitle import RecordTitle
from src.RecordLifecycle.domain.ValueObjects.CreationDate import CreationDate
from src.RecordLifecycle.domain.ValueObjects.VideogameDescription import VideogameDescription
from src.RecordLifecycle.domain.ValueObjects.VideogamePlaytime import VideogamePlaytime
from src.RecordLifecycle.domain.ValueObjects.VideogameRating import VideogameRating
from ..Persistance.VideogameRecordRepositoryImpl import VideogameRecordRepositoryImpl
from pydantic import BaseModel
import uuid

class CreateVidegameRecordRequest(BaseModel):
    author: str
    title: str
    date: str
    description: str
    playtime: int
    rating: float | int

def create_videogame_record(create_request: CreateVidegameRecordRequest, repository: VideogameRecordRepositoryImpl):
    try:
        command = CreateVideogameRecordCommand(AuthorId(create_request.author), RecordTitle(create_request.title), CreationDate(create_request.date), VideogameDescription(create_request.description), VideogamePlaytime(create_request.playtime), VideogameRating(create_request.rating), RecordId(str(uuid.UUID(version=4))))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None

    handler = CreateVideogameRecordHandler(repository)
    
    handler.handle(command)
    return command.id