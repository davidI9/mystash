from src.RecordLifecycle.domain.ValueObjects import RecordId
from src.RecordLifecycle.application.UseCases.VideogameRecord.DeleteVideogameRecord.DeleteVideogameRecordCommand import DeleteVideogameRecordCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.DeleteVideogameRecord.DeleteVideogameRecordHandler import DeleteVideogameRecordHandler
from ..Persistance.VideogameRecordRepositoryImpl import VideogameRecordRepositoryImpl

def delete_videogame_record_by_id(id: str, connection_url: str):
    repository = VideogameRecordRepositoryImpl(connection_url)
    command = DeleteVideogameRecordCommand(RecordId(id))
    handler = DeleteVideogameRecordHandler(repository)
    
    handler.handle(command)