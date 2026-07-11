from abc import ABC, abstractmethod
from src.RecordLifecycle.domain.Entities.VideogameRecord import VideogameRecord
from src.RecordLifecycle.domain.ValueObjects import AuthorId, RecordId

class VideogameRecordRepository(ABC):
    
    @abstractmethod
    def save(self, record: VideogameRecord):
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