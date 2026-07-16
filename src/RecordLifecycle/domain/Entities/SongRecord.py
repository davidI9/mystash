from dataclasses import dataclass
from ..ValueObjects.RecordTitle import RecordTitle
from ..ValueObjects.CreationDate import CreationDate
from ..ValueObjects.RecordId import RecordId
from ..ValueObjects.AuthorId import AuthorId
from ..ValueObjects.ArtistName import ArtistName
from ..ValueObjects.GenreName import GenreName
from ..ValueObjects.SongDuration import SongDuration


@dataclass
class SongRecord():
    author: AuthorId 
    song_title: RecordTitle
    date: CreationDate
    id: RecordId
    artist: ArtistName
    main_genre: GenreName
    duration: SongDuration
    album_id: RecordId | None = None    
    
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

    def set_artist(self, new_artist):
        if not isinstance(new_artist, ArtistName):
            raise TypeError("The new artist must be an ArtistName type object.")
        self.artist = new_artist

    def get_artist(self):
        return self.artist

    def set_album(self, new_album):
        if not isinstance(new_album, RecordId) and new_album is not None:
            raise TypeError("The new album must be an RecordId type object or None.")
        self.album = new_album

    def get_album(self):
        return self.album

    def set_main_genre(self, new_genre):
        if not isinstance(new_genre, GenreName):
            raise TypeError("The new genre must be a GenreName type object.")
        self.main_genre = new_genre

    def get_main_genre(self):
        return self.main_genre

    def set_duration(self, new_duration):
        if not isinstance(new_duration, SongDuration):
            raise TypeError("The new duration must be a SongDuration type object.")
        self.duration = new_duration

    def get_duration(self):
        return self.duration
    
    def __eq__(self, value):
        return isinstance(value, SongRecord) and self.id == value.id and self.author == value.author