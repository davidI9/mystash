from uuid import uuid4

class AuthorId:
    def __init__(self):
        self._id = uuid4()
    
    def __repr__(self):
        return str(self._id)
    
    def __eq__(self, value):
        return isinstance(self, value) and self._id == value._id
    
    def __str__(self) -> str:
        return str(self._id)