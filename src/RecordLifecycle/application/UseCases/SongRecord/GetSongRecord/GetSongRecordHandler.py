from .GetSongRecordCommand import GetSongRecordCommand
from src.RecordLifecycle.domain.Repositories.SongRecordRepository import SongRecordRepository

class GetSongRecordHandler:
    def __init__(self, repository: SongRecordRepository):
        self.repository = repository

    def handle(self, command: GetSongRecordCommand):
        try:
            record = self.repository.get_by_id(command.record_id)
            return record
        except Exception as e:
            print(f"An error has ocurred while getting the record: {e}")