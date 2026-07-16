from .UpdateVideogameRecordCommand import UpdateVideogameRecordCommand
from src.RecordLifecycle.domain.Repositories.VideogameRecordRepository import VideogameRecordRepository
from src.RecordLifecycle.domain.Entities.VideogameRecord import VideogameRecord

class UpdateVideogameRecordHandler:
    def __init__(self, repository: VideogameRecordRepository):
        self.repository = repository

    def handle(self, command: UpdateVideogameRecordCommand):
        self.record = VideogameRecord(command.author_id, command.game_title, command.date, command.id, command.description, command.rating, command.playtime)
        try:
            self.repository.update_record(self.record)
        except Exception as e:
            print(f"An error has ocurred while updating the record: {e}")