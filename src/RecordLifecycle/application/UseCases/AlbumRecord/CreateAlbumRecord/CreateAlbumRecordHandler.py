from .CreateAlbumRecordCommand import CreateAlbumRecordCommand
from src.RecordLifecycle.domain.Entities.AlbumRecord import AlbumRecord
from src.RecordLifecycle.domain.Repositories.AlbumRecordRepository import AlbumRecordRepository

class CreateAlbumRecordHandler:
    
    def __init__(self, repository: AlbumRecordRepository):
        self.repository = repository

    def handle(self, command: CreateAlbumRecordCommand):
        self.album_record = AlbumRecord(command.author, command.album_title, command.date, command.id, command.artist, command.main_genre)
        try:
            self.repository.save(self.album_record)
        except Exception as e:
            print(f"Error saving album record: {e}")
            raise Exception(f"Error saving album record: {e}")