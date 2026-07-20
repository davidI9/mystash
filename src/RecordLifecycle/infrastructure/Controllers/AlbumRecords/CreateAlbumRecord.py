from fastapi import APIRouter
from pydantic import BaseModel
from src.RecordLifecycle.application.UseCases.AlbumRecord.CreateAlbumRecord.CreateAlbumRecordCommand import CreateAlbumRecordCommand
from src.RecordLifecycle.application.UseCases.AlbumRecord.CreateAlbumRecord.CreateAlbumRecordHandler import CreateAlbumRecordHandler
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from src.RecordLifecycle.domain.ValueObjects.RecordTitle import RecordTitle
from src.RecordLifecycle.domain.ValueObjects.CreationDate import CreationDate
from src.RecordLifecycle.domain.ValueObjects.ArtistName import ArtistName
from src.RecordLifecycle.domain.ValueObjects.GenreName import GenreName
import uuid

class CreateAlbumRecordRequest(BaseModel):
    author: str 
    album_title: str
    date: str
    artist: str
    main_genre: str
    
def create_album_record_endpoint(handler: CreateAlbumRecordHandler):
    router = APIRouter()
    
    @router.post("/create_record")
    async def create_record(create_request: CreateAlbumRecordRequest):
        try:
            id = create_album_record(create_request, handler)
            return {"id": id}
        except Exception as e:
            print(e)

def create_album_record(create_request: CreateAlbumRecordRequest, handler: CreateAlbumRecordHandler):
    try:
        command = CreateAlbumRecordCommand(AuthorId(create_request.author), RecordTitle(create_request.album_title), CreationDate(create_request.date), RecordId(str(uuid.uuid4())), ArtistName(create_request.artist), GenreName(create_request.main_genre))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    handler.handle(command)
    return command.id