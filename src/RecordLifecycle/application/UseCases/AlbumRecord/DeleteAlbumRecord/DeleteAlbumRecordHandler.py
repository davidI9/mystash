from .DeleteAlbumRecordCommand import DeleteAlbumRecordCommand
from src.RecordLifecycle.domain.Repositories.AlbumRecordRepository import AlbumRecordRepository

class DeleteAlbumRecordHandler:
    def __init__(self, repository: AlbumRecordRepository):
        self.repository = repository

    def handle(self, command: DeleteAlbumRecordCommand):
        try:
            self.repository.delete_by_id(command.record_id)
        except Exception as e:
            print(f"Error deleting album record: {e}")
            raise Exception(f"Error deleting album record: {e}")