from src.RecordLifecycle.application.UseCases.VideogameRecord.GetVideogameRecord.GetVideogameRecordCommand import GetVideogameRecordCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.GetVideogameRecord.GetVideogameRecordHandler import GetVideogameRecordHandler
from src.RecordLifecycle.domain.ValueObjects import RecordId
from fastapi import APIRouter

def create_get_videogame_record_by_id_endpoint(handler: GetVideogameRecordHandler):
    router = APIRouter()

    @router.get("/get/{record_id}")
    async def get_by_id(record_id: str):
        try:
            record = get_videogame_record_by_id(record_id, handler)
            return record
        except Exception as e:
            print(e)

    return router

router = APIRouter()

def get_videogame_record_by_id(id: str, handler: GetVideogameRecordHandler):
    try:
        command = GetVideogameRecordCommand(RecordId(id))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    record = handler.handle(command)
    return record