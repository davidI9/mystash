from abc import ABC, abstractmethod
from ..Entities.AlbumRecord import AlbumRecord
from ..ValueObjects.AuthorId import AuthorId
from ..ValueObjects.RecordId import RecordId

class AlbumRecordRepository(ABC):
    
    @abstractmethod
    def save(self, record: AlbumRecord):
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
    def update_record(self, record: AlbumRecord):
        pass