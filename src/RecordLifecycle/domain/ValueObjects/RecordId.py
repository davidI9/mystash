import uuid

class RecordId:
    def __init__(self, record_id: str):
        try:
            holder = uuid.UUID(record_id, version=4)
            self.id = str(holder)
        except ValueError:
            raise ValueError("Invalid record ID")
    
    def __repr__(self):
        return str(self.id)
    
    def __eq__(self, value):
        return isinstance(value, RecordId) and self.id == value.id
    
    def __str__(self) -> str:
        return str(self.id)