from ..Entities.SongRecord import SongRecord

class TrackList:
    def __init__(self, tracks: list[SongRecord] | None = None):
        if not isinstance(tracks, list | None):
            raise ValueError("Tracks must be a list.")
        
        if tracks is None:
            tracks = []
        
        else:
            for track in tracks:
                if not isinstance(track, SongRecord):
                    raise TypeError("All tracks must be instances of SongRecord.")
            
        self.tracks = tracks

    def __eq__(self, other):
        if isinstance(other, TrackList):
            return self.tracks == other.tracks
        return False
    
    def __str__(self):  
        return str(self.tracks)
    
    @property
    def _tracks(self):
        return self.tracks
    
    def get_total_duration(self):
        if not self.tracks:
            return 0
        total_duration = sum(track.duration._duration for track in self.tracks)
        return total_duration

    def get_song_count(self):
        return len(self.tracks)