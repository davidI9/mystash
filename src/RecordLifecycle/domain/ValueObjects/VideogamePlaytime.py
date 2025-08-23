#in minutes
class VideogamePlaytime:
    def __init__(self, playtime):
        if not isinstance(playtime, (int, float)):
            raise TypeError("Playtime should be either an int or a float")
            
        if playtime >=0:
            self._playtime = playtime
            
        else:
            raise ValueError("Playtime must be at least 0")
    
    def __eq__(self, value):
        return isinstance(value, VideogamePlaytime) and self._playtime == value._playtime
    
    def __repr__(self):
        return str(self._playtime)
    
    def __int__(self):
        return int(self._playtime)