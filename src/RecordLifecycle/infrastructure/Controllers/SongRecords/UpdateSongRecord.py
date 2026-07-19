from fastapi import APIRouter
from pydantic import BaseModel
from src.RecordLifecycle.application.UseCases.SongRecord.UpdateSongRecord.UpdateSongRecordCommand import UpdateSongRecordCommand
from src.RecordLifecycle.application.UseCases.SongRecord.UpdateSongRecord.UpdateSongRecordHandler import UpdateSongRecordHandler
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from src.RecordLifecycle.domain.ValueObjects.RecordTitle import RecordTitle
from src.RecordLifecycle.domain.ValueObjects.CreationDate import CreationDate
from src.RecordLifecycle.domain.ValueObjects.SongDuration import SongDuration
from src.RecordLifecycle.domain.ValueObjects.ArtistName import ArtistName
from src.RecordLifecycle.domain.ValueObjects.GenreName import GenreName

class UpdateSongRecordRequest(BaseModel):
    author: str 
    song_title: str
    date: str
    id: str
    artist: str
    main_genre: str
    duration: int
    album_id: str | None = None
    
def update_song_record_endpoint(handler: UpdateSongRecordHandler):
    router = APIRouter()

    @router.post("/update_record")
    async def update_record(update_request: UpdateSongRecordRequest):
        try:
            id = update_song_record(update_request, handler)
            return {"id": id}
        except Exception as e:
            print(e)

    return router

def update_song_record(update_request: UpdateSongRecordRequest, handler: UpdateSongRecordHandler):
    try:
        command = UpdateSongRecordCommand(
            AuthorId(update_request.author),
            RecordTitle(update_request.song_title),
            CreationDate(update_request.date),
            RecordId(update_request.id),
            ArtistName(update_request.artist),
            GenreName(update_request.main_genre),
            SongDuration(update_request.duration),
            RecordId(update_request.album_id) if update_request.album_id else None
        )
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    handler.handle(command)
    return command.id