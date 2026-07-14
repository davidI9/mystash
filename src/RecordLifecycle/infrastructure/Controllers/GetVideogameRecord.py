from src.RecordLifecycle.application.UseCases.VideogameRecord.GetVideogameRecord.GetVideogameRecordCommand import GetVideogameRecordCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.GetVideogameRecord.GetVideogameRecordHandler import GetVideogameRecordHandler
from ..Persistance.VideogameRecordRepositoryImpl import VideogameRecordRepositoryImpl
from src.RecordLifecycle.domain.ValueObjects import RecordId

def get_videogame_record_by_id(id: str, repository: VideogameRecordRepositoryImpl):
    try:
        command = GetVideogameRecordCommand(RecordId(id))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None

    handler = GetVideogameRecordHandler(repository)
    
    record = handler.handle(command)
    return record