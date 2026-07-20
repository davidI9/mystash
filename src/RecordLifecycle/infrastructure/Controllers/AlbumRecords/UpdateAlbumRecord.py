from fastapi import APIRouter
from pydantic import BaseModel
from src.RecordLifecycle.application.UseCases.AlbumRecord.UpdateAlbumRecord.UpdateAlbumRecordCommand import UpdateAlbumRecordCommand
from src.RecordLifecycle.application.UseCases.AlbumRecord.UpdateAlbumRecord.UpdateAlbumRecordHandler import UpdateAlbumRecordHandler
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from src.RecordLifecycle.domain.ValueObjects.RecordTitle import RecordTitle
from src.RecordLifecycle.domain.ValueObjects.CreationDate import CreationDate
from src.RecordLifecycle.domain.ValueObjects.ArtistName import ArtistName
from src.RecordLifecycle.domain.ValueObjects.GenreName import GenreName

class UpdateAlbumRecordRequest(BaseModel):
    author: str 
    album_title: str
    date: str
    id: str
    artist: str
    main_genre: str
    
def update_album_record_endpoint(handler: UpdateAlbumRecordHandler):
    router = APIRouter()

    @router.post("/update_record")
    async def update_record(update_request: UpdateAlbumRecordRequest):
        try:
            id = update_album_record(update_request, handler)
            return {"id": id}
        except Exception as e:
            print(e)

    return router

def update_album_record(update_request: UpdateAlbumRecordRequest, handler: UpdateAlbumRecordHandler):
    try:
        command = UpdateAlbumRecordCommand(AuthorId(update_request.author), RecordTitle(update_request.album_title), CreationDate(update_request.date), RecordId(update_request.id), ArtistName(update_request.artist), GenreName(update_request.main_genre))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    handler.handle(command)
    return command.id