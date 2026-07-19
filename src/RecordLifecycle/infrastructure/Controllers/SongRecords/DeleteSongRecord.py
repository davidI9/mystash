from fastapi import APIRouter
from pydantic import BaseModel
from src.RecordLifecycle.application.UseCases.SongRecord.DeleteSongRecord.DeleteSongRecordCommand import DeleteSongRecordCommand
from src.RecordLifecycle.application.UseCases.SongRecord.DeleteSongRecord.DeleteSongRecordHandler import DeleteSongRecordHandler
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId

def create_delete_song_record_endpoint(handler: DeleteSongRecordHandler):
    router = APIRouter()

    @router.delete("/delete_record/{record_id}")
    async def delete_record(record_id: str):
        try:
            delete_song_record(record_id, handler)
            return {"message": "Record deleted successfully"}
        except Exception as e:
            print(e)
            return {"error": str(e)}

    return router

def delete_song_record(id: str, handler: DeleteSongRecordHandler):
    try:
        command = DeleteSongRecordCommand(RecordId(id))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    handler.handle(command)