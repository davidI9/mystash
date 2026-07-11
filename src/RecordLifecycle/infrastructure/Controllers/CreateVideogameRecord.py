from src.RecordLifecycle.application.UseCases.VideogameRecord.CreateVideogameRecord.CreateVideogameRecordCommand import CreateVideogameRecordCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.CreateVideogameRecord.CreateVideogameRecordHandler import CreateVideogameRecordHandler
from src.RecordLifecycle.domain.ValueObjects import AuthorId, CreationDate, RecordId, RecordTitle, VideogameDescription, VideogamePlaytime, VideogameRating
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

def create_videogame_record(create_request: CreateVidegameRecordRequest, connection_url: str):
    
    repository = VideogameRecordRepositoryImpl(connection_url)
    command = CreateVideogameRecordCommand(AuthorId(create_request.author), RecordTitle(create_request.title), CreationDate(create_request.date), VideogameDescription(create_request.description), VideogamePlaytime(create_request.playtime), VideogameRating(create_request.rating), RecordId(uuid.UUID(version=4)))
    handler = CreateVideogameRecordHandler(repository)
    
    handler.handle(command)
    return command.id