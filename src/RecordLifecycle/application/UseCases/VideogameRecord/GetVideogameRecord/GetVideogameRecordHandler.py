from .GetVideogameRecordCommand import GetVideogameRecordCommand
from src.RecordLifecycle.domain.Repositories.VideogameRecordRepository import VideogameRecordRepository
from src.RecordLifecycle.domain.Entities.VideogameRecord import VideogameRecord

#FALTAN LAS PUBLICACIONES DE EVENTOS DE DOMINIO

class GetVideogameRecordHandler:
    
    def __init__(self, repository: VideogameRecordRepository):
        self.repository = repository
    
    def handle(self, command: GetVideogameRecordCommand) -> VideogameRecord | None:
        
        try:
            record = self.repository.get_by_id(command.id)
            return record
        
        except Exception as e:
            print(f"An error has ocurred while getting the record: {e}")