from fastapi import APIRouter
from src.RecordLifecycle.application.UseCases.AlbumRecord.DeleteAlbumRecord.DeleteAlbumRecordCommand import DeleteAlbumRecordCommand
from src.RecordLifecycle.application.UseCases.AlbumRecord.DeleteAlbumRecord.DeleteAlbumRecordHandler import DeleteAlbumRecordHandler
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId

def create_delete_album_record_endpoint(handler: DeleteAlbumRecordHandler):
    router = APIRouter()

    @router.delete("/delete_record/{record_id}")
    async def delete_record(record_id: str):
        try:
            delete_album_record(record_id, handler)
            return {"message": "Record deleted successfully"}
        except Exception as e:
            print(e)
            return {"error": str(e)}

    return router

def delete_album_record(id: str, handler: DeleteAlbumRecordHandler):
    try:
        command = DeleteAlbumRecordCommand(RecordId(id))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    handler.handle(command)