from pymongo.database import Database
from src.RecordLifecycle.domain.Repositories.AlbumRecordRepository import AlbumRecordRepository
from src.RecordLifecycle.domain.Entities.AlbumRecord import AlbumRecord
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from .AlbumMongodbRepo import AlbumMongodbRepo

class AlbumRecordRepositoryImpl(AlbumRecordRepository):
    
    def __init__(self, database: Database):
        self.album_records_db = AlbumMongodbRepo(database)
    
    def save(self, record: AlbumRecord):
        self.album_records_db.save_in_db(record)
    
    def get_by_id(self, id: RecordId):
        return self.album_records_db.get_by_id_from_db(id)
    
    def delete_by_id(self, id: RecordId):
        return self.album_records_db.delete_by_id(id)
    
    def get_user_records(self, author_id: AuthorId):
        return self.album_records_db.get_user_records(author_id)
    
    def update_record(self, record: AlbumRecord):
        return self.album_records_db.update_record(record)