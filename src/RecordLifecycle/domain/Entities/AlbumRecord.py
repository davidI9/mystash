from dataclasses import dataclass

from src.RecordLifecycle.domain.ValueObjects.SongDuration import SongDuration
from ..ValueObjects.RecordTitle import RecordTitle
from ..ValueObjects.CreationDate import CreationDate
from ..ValueObjects.RecordId import RecordId
from ..ValueObjects.AuthorId import AuthorId
from ..ValueObjects.ArtistName import ArtistName
from ..ValueObjects.GenreName import GenreName

@dataclass
class AlbumRecord:
    author: AuthorId 
    album_title: RecordTitle
    date: CreationDate
    id: RecordId
    artist: ArtistName
    main_genre: GenreName

    def get_id(self):
        return self.id

    def get_author(self):
        return self.author

    def set_album_title(self, new_title: RecordTitle):
        if not isinstance(new_title, RecordTitle):
            raise TypeError("The new title must be a RecordTitle type object.")
        self.album_title = new_title

    def get_album_title(self):
        return self.album_title

    def set_date(self, new_date: CreationDate):
        if not isinstance(new_date, CreationDate):
            raise TypeError("The new date must be a CreationDate type object.")
        self.date = new_date
    
    def get_date(self):
        return self.date

    def set_artist(self, new_artist):
        if not isinstance(new_artist, ArtistName):
            raise TypeError("The new artist must be an ArtistName type object.")
        self.artist = new_artist

    def get_artist(self):
        return self.artist

    def set_main_genre(self, new_genre):
        if not isinstance(new_genre, GenreName):
            raise TypeError("The new genre must be a GenreName type object.")
        self.main_genre = new_genre

    def get_main_genre(self):
        return self.main_genre
    
    def __eq__(self, value):
        return isinstance(value, AlbumRecord) and self.id == value.id and self.author == value.author