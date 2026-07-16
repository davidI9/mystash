from src.RecordLifecycle.domain.Entities.VideogameRecord import VideogameRecord
from src.RecordLifecycle.domain.ValueObjects import RecordTitle, VideogameDescription, VideogamePlaytime, VideogameRating, AuthorId, CreationDate
from src.RecordLifecycle.domain.Repositories.VideogameRecordRepository import VideogameRecordRepository
from .CreateVideogameRecordCommand import CreateVideogameRecordCommand

class CreateVideogameRecordHandler:
    def __init__(self, repository: VideogameRecordRepository):
        self.repository = repository
    
    def handle(self, command: CreateVideogameRecordCommand):        
        self.VideogameRecord = VideogameRecord(command.author, command.game_title, command.date, command.id, command.description, command.rating, command.playtime)

        try:
            self.repository.save(self.VideogameRecord)
            
        except Exception as e:
            print(f"An error has ocurred while saving the record: {e}")