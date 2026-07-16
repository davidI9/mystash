from dataclasses import dataclass
from ..ValueObjects.VideogameDescription import VideogameDescription
from ..ValueObjects.VideogameRating import VideogameRating
from ..ValueObjects.VideogamePlaytime import VideogamePlaytime
from ..ValueObjects.RecordTitle import RecordTitle
from ..ValueObjects.CreationDate import CreationDate
from ..ValueObjects.RecordId import RecordId
from ..ValueObjects.AuthorId import AuthorId

@dataclass
class VideogameRecord():
    author: AuthorId 
    game_title: RecordTitle
    date: CreationDate
    id: RecordId
    description: VideogameDescription
    rating: VideogameRating
    playtime: VideogamePlaytime
    
    def get_id(self):
        return self.id

    def get_author(self):
        return self.author

    def set_game_title(self, new_game_title: RecordTitle):
        if not isinstance(new_game_title, RecordTitle):
            raise TypeError("The new title must be a RecordTitle type object.")
        self.game_title = new_game_title

    def get_game_title(self):
        return self.game_title

    def set_date(self, new_date: CreationDate):
        if not isinstance(new_date, CreationDate):
            raise TypeError("The new date must be a CreationDate type object.")
        self.date = new_date
    
    def get_date(self):
        return self.date
    
    def set_description(self, new_description):
        if not isinstance(new_description, VideogameDescription):
            raise TypeError("The new description must be a VideogameDescription type object.")
        self.description = new_description
    
    def get_description(self):
        return self.description
    
    def set_rating(self, new_rating):
        if not isinstance(new_rating, VideogameRating):
            raise TypeError("The new rating must be a VideogameRating type object.")
        self.rating = new_rating
    
    def get_rating(self):
        return self.rating
    
    def set_playtime(self, new_playtime):
        if not isinstance(new_playtime, VideogamePlaytime):
            raise TypeError("The new playtime must be a VideogamePlaytime type object.")
        self.playtime = new_playtime
    
    def get_playtime(self):
        return self.playtime

    def __eq__(self, value):
        return isinstance(value, VideogameRecord) and self.id == value.id and self.author == value.author    