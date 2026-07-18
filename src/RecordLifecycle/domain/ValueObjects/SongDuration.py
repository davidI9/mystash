class SongDuration:
    def __init__(self, duration: int):
        if not isinstance(duration, int):
            raise TypeError("Duration must be an integer representing seconds.")
        if duration < 0 or duration > 3600:
            raise ValueError("Duration must be a positive integer between 0 and 3600.")
        self.duration = duration

    def __eq__(self, other):
        if isinstance(other, SongDuration):
            return self.duration == other.duration
        return False
    
    def __str__(self):  
        return str(self.duration)
    
    @property
    def _duration(self):
        return self.duration