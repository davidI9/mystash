from src.RecordLifecycle.domain.ValueObjects import RecordId
from src.RecordLifecycle.application.UseCases.VideogameRecord.DeleteVideogameRecord.DeleteVideogameRecordCommand import DeleteVideogameRecordCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.DeleteVideogameRecord.DeleteVideogameRecordHandler import DeleteVideogameRecordHandler
from fastapi import APIRouter

def delete_videogame_record_by_id_endpoint(handler: DeleteVideogameRecordHandler):
    router = APIRouter()

    @router.delete("/VideogamesRecords/delete/{record_id}")
    async def delete_record(record_id: str):
        try:
            delete_videogame_record_by_id(record_id, handler)
        except Exception as e:
            print(e)

    return router

def delete_videogame_record_by_id(id: str, handler: DeleteVideogameRecordHandler):
    try:
        command = DeleteVideogameRecordCommand(RecordId(id))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    
    handler.handle(command)