from pymongo.database import Database
from src.RecordLifecycle.domain.Repositories.VideogameRecordRepository import VideogameRecordRepository
from src.RecordLifecycle.domain.Entities.VideogameRecord import VideogameRecord
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from .VideogameMongodbRepo import VideogameMongodbRepo

class VideogameRecordRepositoryImpl(VideogameRecordRepository):
    
    def __init__(self, database: Database):
        self.videogame_records_db = VideogameMongodbRepo(database)
    
    def save(self, record: VideogameRecord):
        self.videogame_records_db.save_in_db(record)
    
    def get_by_id(self, id: RecordId):
        return self.videogame_records_db.get_by_id_from_db(id)
    
    def delete_by_id(self, id: RecordId):
        return self.videogame_records_db.delete_by_id(id)
    
    def get_user_records(self, author_id: AuthorId):
        return self.videogame_records_db.get_user_records(author_id)
    
    def update_record(self, record: VideogameRecord):
        return self.videogame_records_db.update_record(record)