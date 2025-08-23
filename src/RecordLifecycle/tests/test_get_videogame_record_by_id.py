from src.RecordLifecycle.application.UseCases.VideogameRecord.GetVideogameRecord.GetVideogameRecordCommand import GetVideogameRecordCommand
from src.RecordLifecycle.application.UseCases.VideogameRecord.GetVideogameRecord.GetVideogameRecordHandler import GetVideogameRecordHandler
from src.RecordLifecycle.domain.ValueObjects import RecordTitle, VideogameDescription, VideogamePlaytime, VideogameRating, CreationDate
from src.RecordLifecycle.domain.VideogameRecord import VideogameRecord
from src.RecordLifecycle.application.Repositories.VideogameRecordRepository import VideogameRecordRepository

class fake_repo_impl(VideogameRecordRepository):
    def save(self, record):
        pass
    
    def get_by_id(self, id):
        if id == "550e8400-e29b-41d4-a716-446655440005":
            return VideogameRecord("550e8400-e29b-41d4-a716-446655440002", RecordTitle("Test"), CreationDate("11/06/2006"), id, VideogameDescription("Test description"), VideogameRating(2), VideogamePlaytime(123))
        return None
    
    def delete_by_id(self, id):
        pass
    

def test_get_videogame_record_by_id():
    
    #arrange
        repository = fake_repo_impl()
        command = GetVideogameRecordCommand("550e8400-e29b-41d4-a716-446655440005")
        handler = GetVideogameRecordHandler(repository)
        
    #act
        record = handler.handle(command)
    
    #assert
        assert(record.get_author() == "550e8400-e29b-41d4-a716-446655440002" 
               and record.get_title() == RecordTitle("Test") 
               and record.get_date() == CreationDate("11/06/2006") 
               and record.get_description() == VideogameDescription("Test description")
               and record.get_rating() == VideogameRating(2)
               and record.get_playtime() == VideogamePlaytime(123))