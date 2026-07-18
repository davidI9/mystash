class  AlbumDuration:
    def __init__(self, duration: int):
        if not isinstance(duration, int):
            raise TypeError("Duration must be an integer representing seconds.")
        if duration < 0 or duration > 60000:
            raise ValueError("Duration must be a positive integer between 0 and 60000.")
        self._duration = duration

    @property
    def duration(self) -> int:
        return self._duration
    
    def __eq__(self, other):
        if isinstance(other, AlbumDuration):
            return self._duration == other._duration
        return False
    
    def __str__(self):
        return str(self._duration)