from .DeleteSongeRecordCommand import DeleteSongRecordCommand
from src.RecordLifecycle.domain.Repositories.SongRecordRepository import SongRecordRepository

class DeleteSongRecordHandler:
    def __init__(self, repository: SongRecordRepository):
        self.repository = repository

    def handle(self, command: DeleteSongRecordCommand):
        try:
            self.repository.delete_by_id(command.record_id)
        except Exception as e:
            print(f"An error has occurred while deleting the record: {e}")