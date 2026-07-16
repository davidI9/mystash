from src.RecordLifecycle.application.UseCases.VideogameRecord.UpdateVideogameRecord.UpdateVideogameRecordCommand import UpdateVideogameRecordCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.UpdateVideogameRecord.UpdateVideogameRecordHandler import UpdateVideogameRecordHandler
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from src.RecordLifecycle.domain.ValueObjects.RecordTitle import RecordTitle
from src.RecordLifecycle.domain.ValueObjects.CreationDate import CreationDate
from src.RecordLifecycle.domain.ValueObjects.VideogameDescription import VideogameDescription
from src.RecordLifecycle.domain.ValueObjects.VideogamePlaytime import VideogamePlaytime
from src.RecordLifecycle.domain.ValueObjects.VideogameRating import VideogameRating
from fastapi import APIRouter
from pydantic import BaseModel

class UpdateVideogameRecordRequest(BaseModel):
    id: str
    author_id: str
    title: str
    date: str
    description: str
    rating: float | int
    playtime: int
    
def update_videogame_record_endpoint(handler: UpdateVideogameRecordHandler):
    router = APIRouter()

    @router.post("/update_record")
    async def update_record(update_request: UpdateVideogameRecordRequest):
        try:
            id = update_videogame_record(update_request, handler)
            return {"id": id}
        except Exception as e:
            print(e)

    return router

def update_videogame_record(update_request: UpdateVideogameRecordRequest, handler: UpdateVideogameRecordHandler):
    try:
        command = UpdateVideogameRecordCommand(RecordId(update_request.id), AuthorId(update_request.author_id), RecordTitle(update_request.title), VideogameDescription(update_request.description), VideogamePlaytime(update_request.playtime), VideogameRating(update_request.rating), CreationDate(update_request.date))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    handler.handle(command)
    return command.id