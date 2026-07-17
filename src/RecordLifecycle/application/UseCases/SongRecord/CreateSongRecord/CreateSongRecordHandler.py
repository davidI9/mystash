from .CreateSongRecordCommand import CreateSongRecordCommand
from src.RecordLifecycle.domain.Entities.SongRecord import SongRecord

class CreateSongRecordHandler:
    def __init__(self, repository):
        self.repository = repository

    def handle(self, command: CreateSongRecordCommand):
        self.record = SongRecord(command.author, command.song_title, command.date, command.id, command.artist, command.main_genre, command.duration, command.album_id)
        
        try:
            self.repository.save_record(self.record)
        except Exception as e:
            print(f"An error has ocurred while saving the record: {e}")