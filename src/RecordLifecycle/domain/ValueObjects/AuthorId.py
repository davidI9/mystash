import uuid

class AuthorId:
    def __init__(self, author_id: str):
        try:
            uuid_obj = uuid.UUID(author_id, version=4)
            self._id = str(uuid_obj)
        except ValueError:
            raise ValueError("Invalid author ID")

    def __repr__(self):
        return str(self._id)
    
    def __eq__(self, value):
        return isinstance(self, value) and self._id == value._id
    
    def __str__(self) -> str:
        return str(self._id)