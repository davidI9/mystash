import uuid

class RecordId:
    def __init__(self, record_id: str):
        try:
            holder = uuid.UUID(record_id, version=4)
            self._id = str(holder)
        except ValueError:
            raise ValueError("Invalid record ID")
    
    def __repr__(self):
        return str(self._id)
    
    def __eq__(self, value):
        return isinstance(self, value) and self._id == value._id
    
    def __str__(self) -> str:
        return str(self._id)