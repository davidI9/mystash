from src.RecordLifecycle.application.UseCases.VideogameRecord.UpdateVideogameRecord.UpdateVideogameRecordCommand import UpdateVideogameRecordCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.UpdateVideogameRecord.UpdateVideogameRecordHandler import UpdateVideogameRecordHandler
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from src.RecordLifecycle.domain.ValueObjects.RecordTitle import RecordTitle
from src.RecordLifecycle.domain.ValueObjects.CreationDate import CreationDate
from src.RecordLifecycle.domain.ValueObjects.VideogameDescription import VideogameDescription
from src.RecordLifecycle.domain.ValueObjects.VideogamePlaytime import VideogamePlaytime
from src.RecordLifecycle.domain.ValueObjects.VideogameRating import VideogameRating
from ..Persistance.VideogameRecordRepositoryImpl import VideogameRecordRepositoryImpl
from pydantic import BaseModel

class UpdateVideogameRecordRequest(BaseModel):
    id: str
    author_id: str
    title: str
    description: str
    playtime: int
    rating: float | int
    date: str

def update_videogame_record(update_request: UpdateVideogameRecordRequest, repository: VideogameRecordRepositoryImpl):
    try:
        command = UpdateVideogameRecordCommand(RecordId(update_request.id), AuthorId(update_request.author_id), RecordTitle(update_request.title), VideogameDescription(update_request.description), VideogamePlaytime(update_request.playtime), VideogameRating(update_request.rating), CreationDate(update_request.date))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None

    handler = UpdateVideogameRecordHandler(repository)
    
    handler.handle(command)
    return command.id