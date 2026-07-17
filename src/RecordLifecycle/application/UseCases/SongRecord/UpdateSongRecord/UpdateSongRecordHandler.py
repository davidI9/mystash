from .UpdateSongRecordCommand import UpdateSongRecordCommand
from src.RecordLifecycle.domain.Entities.SongRecord import SongRecord
from src.RecordLifecycle.domain.Repositories.SongRecordRepository import SongRecordRepository

class UpdateSongRecordHandler:
    def __init__(self, repository: SongRecordRepository):
        self.repository = repository

    def handle(self, command: UpdateSongRecordCommand):
        self.song_record = SongRecord(command.author, command.song_title, command.date, command.id, command.artist, command.main_genre, command.duration, command.album_id)    
        try:
            self.repository.update_record(self.song_record)
        except Exception as e:
            print(f"An error has occurred while updating the record: {e}")