from src.RecordLifecycle.domain.ValueObjects import RecordId
from src.RecordLifecycle.application.UseCases.VideogameRecord.DeleteVideogameRecord.DeleteVideogameRecordCommand import DeleteVideogameRecordCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.DeleteVideogameRecord.DeleteVideogameRecordHandler import DeleteVideogameRecordHandler
from ..Persistance.VideogameRecordRepositoryImpl import VideogameRecordRepositoryImpl

def delete_videogame_record_by_id(id: str, repository: VideogameRecordRepositoryImpl):
    try:
        command = DeleteVideogameRecordCommand(RecordId(id))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    handler = DeleteVideogameRecordHandler(repository)
    
    handler.handle(command)