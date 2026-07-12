from src.RecordLifecycle.domain.Repositories.VideogameRecordRepository import VideogameRecordRepository
from src.RecordLifecycle.domain.Entities.VideogameRecord import VideogameRecord
from .VideogameMongodbRepo import VideogameMongodbRepo

class VideogameRecordRepositoryImpl(VideogameRecordRepository):
    
    def __init__(self, connection_url: str):
        self.videogame_records_db = VideogameMongodbRepo(connection_url)
    
    def save(self, record: VideogameRecord):
        self.videogame_records_db.save_in_db(record)
    
    def get_by_id(self, id):
        return self.videogame_records_db.get_by_id_from_db(id)
    
    def delete_by_id(self, id):
        return self.videogame_records_db.delete_by_id(id)
    
    def get_user_records(self, author_id):
        return self.videogame_records_db.get_user_records(author_id)
    
    def update_record(self, record: VideogameRecord):
        return self.videogame_records_db.update_record(record)