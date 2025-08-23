from abc import ABC
from dataclasses import dataclass, field
from .ValueObjects.RecordId import RecordId
from .ValueObjects.AuthorId import AuthorId 
from .ValueObjects.RecordTitle import RecordTitle
from .ValueObjects.CreationDate import CreationDate

@dataclass
class Record(ABC):
    
    _author: AuthorId 
    _title: RecordTitle
    _date: CreationDate
    _id: RecordId

    def get_id(self):
        return self._id

    def get_author(self):
        return self._author

    def set_title(self, new_title: RecordTitle):
        if not isinstance(new_title, RecordTitle):
            raise TypeError("The new title must be a RecordTitle type object.")
        self._title = new_title
    
    def get_title(self):
        return self._title
    
    def set_date(self, new_date: CreationDate):
        if not isinstance(new_date, CreationDate):
            raise TypeError("The new date must be a CreationDate type object.")
        self._date = new_date
    
    def get_date(self):
        return self._date
    