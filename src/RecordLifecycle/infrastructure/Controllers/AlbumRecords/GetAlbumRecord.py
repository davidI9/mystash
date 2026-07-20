from fastapi import APIRouter
from src.RecordLifecycle.application.UseCases.AlbumRecord.GetAlbumRecord.GetAlbumRecordCommand import GetAlbumRecordCommand
from src.RecordLifecycle.application.UseCases.AlbumRecord.GetAlbumRecord.GetAlbumRecordHandler import GetAlbumRecordHandler
from src.RecordLifecycle.domain.ValueObjects import RecordId

def get_album_record_endpoint(handler: GetAlbumRecordHandler):
    router = APIRouter()

    @router.get("/get_record/{record_id}")
    async def get_record(record_id: str):
        try:
            record = get_album_record(record_id, handler)
            return record
        except Exception as e:
            print(e)

    return router

def get_album_record(id: str, handler: GetAlbumRecordHandler):
    try:
        command = GetAlbumRecordCommand(RecordId(id))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    record = handler.handle(command)
    return record