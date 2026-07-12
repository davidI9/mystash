from abc import ABC
from dataclasses import dataclass
from ..ValueObjects.RecordId import RecordId
from ..ValueObjects.AuthorId import AuthorId 
from ..ValueObjects.RecordTitle import RecordTitle
from ..ValueObjects.CreationDate import CreationDate

@dataclass
class Record(ABC):
    
    author: AuthorId 
    title: RecordTitle
    date: CreationDate
    id: RecordId

    def get_id(self):
        return self.id

    def get_author(self):
        return self.author

    def set_title(self, new_title: RecordTitle):
        if not isinstance(new_title, RecordTitle):
            raise TypeError("The new title must be a RecordTitle type object.")
        self.title = new_title
    
    def get_title(self):
        return self.title
    
    def set_date(self, new_date: CreationDate):
        if not isinstance(new_date, CreationDate):
            raise TypeError("The new date must be a CreationDate type object.")
        self.date = new_date
    
    def get_date(self):
        return self.date
    
    def __eq__(self, value):
        return isinstance(value, Record) and self.id == value.id and self.author == value.author
    