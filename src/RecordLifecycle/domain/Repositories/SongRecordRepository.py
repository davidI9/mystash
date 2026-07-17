from abc import ABC, abstractmethod
from src.RecordLifecycle.domain.Entities.SongRecord import SongRecord
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId

class SongRecordRepository(ABC):
    
    @abstractmethod
    def save(self, record: SongRecord):
        pass
    
    @abstractmethod
    def get_by_id(self, id: RecordId):
        pass
    
    @abstractmethod
    def delete_by_id(self, id: RecordId):
        pass
    
    @abstractmethod
    def get_user_records(self, author_id: AuthorId):
        pass
    
    @abstractmethod
    def update_record(self, record: SongRecord):
        pass
    
    @abstractmethod
    def get_album_songs(self, album_id: RecordId):
        pass
