from fastapi import APIRouter
from src.RecordLifecycle.application.UseCases.AlbumRecord.GetUserAlbumRecords.GetUserAlbumRecordsCommand import GetUserAlbumRecordsCommand
from src.RecordLifecycle.application.UseCases.AlbumRecord.GetUserAlbumRecords.GetUserAlbumRecordsHandler import GetUserAlbumRecordsHandler
from src.RecordLifecycle.domain.ValueObjects import AuthorId

def get_user_album_records_endpoint(handler: GetUserAlbumRecordsHandler):
    router = APIRouter()

    @router.get("/get_user_records/{author_id}")
    async def get_user_records(author_id: str):
        try:
            records = get_user_album_records(author_id, handler)
            return records
        except Exception as e:
            print(e)

    return router

def get_user_album_records(author_id: str, handler: GetUserAlbumRecordsHandler):
    try:
        command = GetUserAlbumRecordsCommand(AuthorId(author_id))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    records = handler.handle(command)
    return records