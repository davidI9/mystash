from ....Repositories.VideogameRecordRepository import VideogameRecordRepository
from .DeleteVideogameRecordCommand import DeleteVideogameRecordCommand

class DeleteVideogameRecordHandler:
    
    def __init__(self, repository: VideogameRecordRepository):
        self.repository = repository
    
    def handle(self, command: DeleteVideogameRecordCommand):
        try:
            self.repository.delete_by_id(command.id)
            
        except Exception as e:
            print(f"An error has occurred while deleting the record: {e}")