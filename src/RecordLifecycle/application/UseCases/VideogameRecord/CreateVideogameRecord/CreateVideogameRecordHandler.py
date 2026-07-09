from src.RecordLifecycle.domain.Entities.VideogameRecord import VideogameRecord
from src.RecordLifecycle.domain.ValueObjects import RecordTitle, VideogameDescription, VideogamePlaytime, VideogameRating, AuthorId, CreationDate
from src.RecordLifecycle.domain.Repositories.VideogameRecordRepository import VideogameRecordRepository
from .CreateVideogameRecordCommand import CreateVideogameRecordCommand

class CreateVideogameRecordHandler:
    def __init__(self, repository: VideogameRecordRepository):
        self.repository = repository
    
    def handle(self, command: CreateVideogameRecordCommand):
        
        try:
            author = command.author
            title = RecordTitle(command.title)
            date = CreationDate(command.date)
            id = command.id
            description = VideogameDescription(command.description)
            rating = VideogameRating(command.rating)
            playtime = VideogamePlaytime(command.playtime)
            
        except Exception as e:
            print(f"An error has ocurred while asigning the record's arguments: {e}")
        
        self.VideogameRecord = VideogameRecord(author, title, date, id, description, rating, playtime)

        try:
            self.repository.save(self.VideogameRecord)
            
        except Exception as e:
            print(f"An error has ocurred while saving the record: {e}")