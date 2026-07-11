from src.RecordLifecycle.application.UseCases.VideogameRecord.GetVideogameRecord.GetVideogameRecordCommand import GetVideogameRecordCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.GetVideogameRecord.GetVideogameRecordHandler import GetVideogameRecordHandler
from ..Persistance.VideogameRecordRepositoryImpl import VideogameRecordRepositoryImpl
from src.RecordLifecycle.domain.ValueObjects import RecordId

def get_videogame_record_by_id(id: str, connection_url: str):
    repository = VideogameRecordRepositoryImpl(connection_url)
    command = GetVideogameRecordCommand(RecordId(id))
    handler = GetVideogameRecordHandler(repository)
    
    record = handler.handle(command)
    return record