from src.RecordLifecycle.domain.Repositories.VideogameRecordRepository import VideogameRecordRepository

class GetUserVideogameRecordsHandler:
    def __init__(self, repository: VideogameRecordRepository):
        self.repository = repository

    def handle(self, command):
        try:
            records = self.repository.get_user_records(command.author_id)
            return records
        except Exception as e:
            print(f"An error has occurred while fetching user records: {e}")