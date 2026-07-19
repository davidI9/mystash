from fastapi import APIRouter
from pydantic import BaseModel
from src.RecordLifecycle.application.UseCases.SongRecord.CreateSongRecord.CreateSongRecordCommand import CreateSongRecordCommand
from src.RecordLifecycle.application.UseCases.SongRecord.CreateSongRecord.CreateSongRecordHandler import CreateSongRecordHandler
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from src.RecordLifecycle.domain.ValueObjects.RecordTitle import RecordTitle
from src.RecordLifecycle.domain.ValueObjects.CreationDate import CreationDate
from src.RecordLifecycle.domain.ValueObjects.SongDuration import SongDuration
from src.RecordLifecycle.domain.ValueObjects.ArtistName import ArtistName
from src.RecordLifecycle.domain.ValueObjects.GenreName import GenreName
import uuid

class CreateSongRecordRequest(BaseModel):
    author: str 
    song_title: str
    date: str
    artist: str
    main_genre: str
    duration: int
    album_id: str | None = None
    
def create_song_record_endpoint(handler: CreateSongRecordHandler):
    router = APIRouter()

    @router.post("/create_record")
    async def create_record(create_request: CreateSongRecordRequest):
        try:
            id = create_song_record(create_request, handler)
            return {"id": id}
        except Exception as e:
            print(e)

    return router

def create_song_record(create_request: CreateSongRecordRequest, handler: CreateSongRecordHandler):
    try:
        command = CreateSongRecordCommand(
            AuthorId(create_request.author),
            RecordTitle(create_request.song_title),
            CreationDate(create_request.date),
            RecordId(str(uuid.uuid4())),
            ArtistName(create_request.artist),
            GenreName(create_request.main_genre),
            SongDuration(create_request.duration),
            RecordId(create_request.album_id) if create_request.album_id else None
        )
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    handler.handle(command)
    return command.id