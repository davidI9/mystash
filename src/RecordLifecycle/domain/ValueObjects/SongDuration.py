class SongDuration:
    def __init__(self, duration: int):
        if not isinstance(duration, int):
            raise TypeError("Duration must be an integer representing seconds.")
        if duration < 0 or duration > 3600:
            raise ValueError("Duration must be a positive integer between 0 and 3600.")
        self.duration = duration

    def get_duration(self):
        return self.duration