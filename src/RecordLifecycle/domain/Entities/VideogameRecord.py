from .Record import Record
from dataclasses import dataclass
from ..ValueObjects.VideogameDescription import VideogameDescription
from ..ValueObjects.VideogameRating import VideogameRating
from ..ValueObjects.VideogamePlaytime import VideogamePlaytime

@dataclass
class VideogameRecord(Record):
    description: VideogameDescription
    rating: VideogameRating
    playtime: VideogamePlaytime
    
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

    
    