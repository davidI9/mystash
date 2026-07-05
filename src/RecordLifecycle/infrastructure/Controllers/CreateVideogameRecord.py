from src.RecordLifecycle.application.UseCases.VideogameRecord.CreateVideogameRecord.CreateVideogameRecordCommand import CreateVideogameRecordCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.CreateVideogameRecord.CreateVideogameRecordHandler import CreateVideogameRecordHandler
from src.RecordLifecycle.domain.ValueObjects import AuthorId
from ..Persistance.VideogameRecordRepositoryImpl import VideogameRecordRepositoryImpl
from pydantic import BaseModel

class CreateVidegameRecordRequest(BaseModel):
    author: str
    title: str
    date: str
    description: str
    playtime: int
    rating: float | int

def create_videogame_record(create_request: CreateVidegameRecordRequest, connection_url: str):
    
    repository = VideogameRecordRepositoryImpl(connection_url)
    command = CreateVideogameRecordCommand(create_request.author, create_request.title, create_request.date, create_request.description, create_request.playtime, create_request.rating)
    handler = CreateVideogameRecordHandler(repository)
    
    handler.handle(command)
    return command.id