from dataclasses import dataclass
from .GetAlbumRecordCommand import GetAlbumRecordCommand
from src.RecordLifecycle.domain.Repositories.AlbumRecordRepository import AlbumRecordRepository
from src.RecordLifecycle.domain.Repositories.SongRecordRepository import SongRecordRepository
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from src.RecordLifecycle.domain.ValueObjects.RecordTitle import RecordTitle
from src.RecordLifecycle.domain.ValueObjects.CreationDate import CreationDate
from src.RecordLifecycle.domain.ValueObjects.ArtistName import ArtistName
from src.RecordLifecycle.domain.ValueObjects.GenreName import GenreName
from src.RecordLifecycle.domain.ValueObjects.AlbumDuration import AlbumDuration
from src.RecordLifecycle.domain.ValueObjects.SongNumber import SongNumber
from src.RecordLifecycle.domain.ValueObjects.TrackList import TrackList

@dataclass
class AlbumRecordResult:
    author: AuthorId 
    album_title: RecordTitle
    date: CreationDate
    id: RecordId
    artist: ArtistName
    main_genre: GenreName
    duration: AlbumDuration
    song_number: SongNumber

class GetAlbumRecordHandler:
    def __init__(self, album_repository: AlbumRecordRepository, song_repository: SongRecordRepository):
        self.album_repository = album_repository
        self.song_repository = song_repository

    def handle(self, command: GetAlbumRecordCommand):
        record = self.album_repository.get_by_id(command.record_id)
        
        try:
            album_songs = TrackList(self.song_repository.get_album_songs(command.record_id))
        except Exception as e:
            print(f"Error occurred while fetching album songs: {e}")
            raise ValueError(f"Error occurred while fetching album songs: {e}")
        
        try:
            result = AlbumRecordResult(AuthorId(record.author), RecordTitle(record.album_title), CreationDate(record.date), RecordId(record.id), ArtistName(record.artist), GenreName(record.main_genre), AlbumDuration(album_songs.get_total_duration()), SongNumber(album_songs.get_song_count()))
        except Exception as e:
            print(f"Error occurred while processing album record: {e}")
            raise ValueError(f"Error occurred while processing album record: {e}")
        
        return result