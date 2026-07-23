from pymongo.database import Database
from src.RecordLifecycle.domain.Repositories.SongRecordRepository import SongRecordRepository
from .SongMongodbRepo import SongMongodbRepo
from src.RecordLifecycle.domain.Entities.SongRecord import SongRecord
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId

class SongRecordRepositoryImpl(SongRecordRepository):
    
    def __init__(self, database: Database):
        self.song_records_db = SongMongodbRepo(database)
    
    def save(self, record: SongRecord):
        self.song_records_db.save_in_db(record)
    
    def get_by_id(self, id: RecordId):
        return self.song_records_db.get_by_id_from_db(id)
    
    def delete_by_id(self, id: RecordId):
        return self.song_records_db.delete_by_id(id)
    
    def get_user_records(self, author_id: AuthorId):
        return self.song_records_db.get_user_records(author_id)
    
    def update_record(self, record: SongRecord):
        return self.song_records_db.update_record(record)
    
    def get_album_songs(self, album_id: RecordId):
        return self.song_records_db.get_album_songs(album_id)