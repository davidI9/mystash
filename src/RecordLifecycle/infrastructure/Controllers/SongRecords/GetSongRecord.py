from fastapi import APIRouter
from src.RecordLifecycle.application.UseCases.SongRecord.GetSongRecord.GetSongRecordCommand import GetSongRecordCommand
from src.RecordLifecycle.application.UseCases.SongRecord.GetSongRecord.GetSongRecordHandler import GetSongRecordHandler
from src.RecordLifecycle.domain.ValueObjects import RecordId

def get_song_record_endpoint(handler: GetSongRecordHandler):
    router = APIRouter()

    @router.get("/get_record/{record_id}")
    async def get_record(record_id: str):
        try:
            record = get_song_record(record_id, handler)
            return record
        except Exception as e:
            print(e)

    return router

def get_song_record(id: str, handler: GetSongRecordHandler):
    try:
        command = GetSongRecordCommand(RecordId(id))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    record = handler.handle(command)
    return record