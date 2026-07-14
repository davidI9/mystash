from pydantic import BaseModel
from src.RecordLifecycle.application.UseCases.VideogameRecord.GetUserVideogameRecords.GetUserVideogameRecordsCommand import GetUserVideogameRecordsCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.GetUserVideogameRecords.GetUserVideogameRecordsHandler import GetUserVideogameRecordsHandler
from src.RecordLifecycle.domain.ValueObjects import AuthorId
from ..Persistance.VideogameRecordRepositoryImpl import VideogameRecordRepositoryImpl
    
def get_user_videogame_records(author_id: str, repository: VideogameRecordRepositoryImpl):
    try:
        command = GetUserVideogameRecordsCommand(AuthorId(author_id))
    except Exception as e:
        print(f"An error has occurred while creating the command: {e}")
        return None
    handler = GetUserVideogameRecordsHandler(repository)
    
    records = handler.handle(command)
    return records