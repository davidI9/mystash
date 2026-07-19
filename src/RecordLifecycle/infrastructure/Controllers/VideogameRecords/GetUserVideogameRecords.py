from src.RecordLifecycle.application.UseCases.VideogameRecord.GetUserVideogameRecords.GetUserVideogameRecordsCommand import GetUserVideogameRecordsCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.GetUserVideogameRecords.GetUserVideogameRecordsHandler import GetUserVideogameRecordsHandler
from src.RecordLifecycle.domain.ValueObjects import AuthorId
from ...Persistance.VideogameRecordRepositoryImpl import VideogameRecordRepositoryImpl
from fastapi import APIRouter

def get_user_videogame_records_endpoint(handler: GetUserVideogameRecordsHandler):
    router = APIRouter()

    @router.get("/get_user_records/{author_id}")
    async def get_user_records(author_id: str):
        try:
            records = get_user_videogame_records(author_id, handler)
            return records
        except Exception as e:
            print(e)

    return router
    
def get_user_videogame_records(author_id: str, handler: GetUserVideogameRecordsHandler):
    try:
        command = GetUserVideogameRecordsCommand(AuthorId(author_id))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    records = handler.handle(command)
    return records