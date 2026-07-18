class SongNumber:
    def __init__(self, number: int):
        if not isinstance(number, int) or number < 0 or number > 2000:
            raise ValueError("Song number must be an integer between 0 and 2000.")
        self.number = number

    def __eq__(self, other):
        if isinstance(other, SongNumber):
            return self.number == other.number
        return False
    
    def __str__(self):  
        return str(self.number)
    
    @property
    def _number(self):
        return self.number