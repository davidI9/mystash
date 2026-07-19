from fastapi import APIRouter
from src.RecordLifecycle.application.UseCases.SongRecord.GetUserSongRecords.GetUserSongRecordsCommand import GetUserSongRecordsCommand
from src.RecordLifecycle.application.UseCases.SongRecord.GetUserSongRecords.GetUserSongRecordsHandler import GetUserSongRecordsHandler
from src.RecordLifecycle.domain.ValueObjects import AuthorId
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId

def get_user_song_records_endpoint(handler: GetUserSongRecordsHandler):
    router = APIRouter()

    @router.get("/get_user_records/{author_id}")
    async def get_user_records(author_id: str):
        try:
            records = get_user_song_records(author_id, handler)
            return records
        except Exception as e:
            print(e)

    return router

def get_user_song_records(author_id: str, handler: GetUserSongRecordsHandler):
    try:
        command = GetUserSongRecordsCommand(AuthorId(author_id))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    records = handler.handle(command)
    return records