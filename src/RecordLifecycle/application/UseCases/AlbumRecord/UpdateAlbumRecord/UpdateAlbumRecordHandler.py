from .UpdateAlbumRecordCommand import UpdateAlbumRecordCommand
from src.RecordLifecycle.domain.Repositories.AlbumRecordRepository import AlbumRecordRepository
from src.RecordLifecycle.domain.Entities.AlbumRecord import AlbumRecord

class UpdateAlbumRecordHandler:
    def __init__(self, repository: AlbumRecordRepository):
        self.repository = repository

    def handle(self, command: UpdateAlbumRecordCommand):
        self.album_record = AlbumRecord(command.author, command.album_title, command.date, command.id, command.artist, command.main_genre)
        
        try:
            self.repository.update_record(self.album_record)
        except Exception as e:
            print(f"An error has occurred while updating the record: {e}")
            raise ValueError(f"An error has occurred while updating the record: {e}")