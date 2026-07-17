from .GetUserSongRecordsCommand import GetUserSongRecordsCommand
from src.RecordLifecycle.domain.Repositories.SongRecordRepository import SongRecordRepository

class GetUserSongRecordsHandler:
    def __init__(self, repository: SongRecordRepository):
        self.repository = repository

    def handle(self, command: GetUserSongRecordsCommand):
        try:
            return self.repository.get_user_records(command.author_id)
        except Exception as e:
            print(f"An error has occurred while retrieving the records: {e}")
            return []