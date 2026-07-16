from src.RecordLifecycle.application.UseCases.VideogameRecord.CreateVideogameRecord.CreateVideogameRecordCommand import CreateVideogameRecordCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.CreateVideogameRecord.CreateVideogameRecordHandler import CreateVideogameRecordHandler
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from src.RecordLifecycle.domain.ValueObjects.RecordTitle import RecordTitle
from src.RecordLifecycle.domain.ValueObjects.CreationDate import CreationDate
from src.RecordLifecycle.domain.ValueObjects.VideogameDescription import VideogameDescription
from src.RecordLifecycle.domain.ValueObjects.VideogamePlaytime import VideogamePlaytime
from src.RecordLifecycle.domain.ValueObjects.VideogameRating import VideogameRating
from fastapi import APIRouter
from pydantic import BaseModel
import uuid

class CreateVidegameRecordRequest(BaseModel):
    author_id: str
    game_title: str
    date: str
    description: str
    rating: float | int
    playtime: int
    
def create_videogame_record_endpoint(handler: CreateVideogameRecordHandler):
    router = APIRouter()

    @router.post("/create_record")
    async def create_record(create_request: CreateVidegameRecordRequest):
        try:
            id = create_videogame_record(create_request, handler)
            return {"id": id}
        except Exception as e:
            print(e)

    return router

def create_videogame_record(create_request: CreateVidegameRecordRequest, handler: CreateVideogameRecordHandler):
    try:
        command = CreateVideogameRecordCommand(AuthorId(create_request.author_id), RecordTitle(create_request.game_title), CreationDate(create_request.date), VideogameDescription(create_request.description), VideogamePlaytime(create_request.playtime), VideogameRating(create_request.rating), RecordId(str(uuid.uuid4())))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    handler.handle(command)
    return command.id