valid_genres = ["Pop", "Rock", "Jazz", "Classical", "Hip Hop", "R&B", "Country", "Electronic", "Reggae", "Blues", "Folk", "Metal", "Punk", "Soul", "Latin", "Funk", "Disco", "Gospel", "World", "Alternative", "Trap", "Rap", "Indie", "K-Pop", "J-Pop", "Ska", "Ambient", "House", "Techno", "Trance", "Dubstep", "Drum and Bass", "Grime", "Chillout", "New Age", "Opera", "Soundtrack", "Video Game Music", "Lo-Fi", "Gothic-Rock", "Post-Rock", "Post-Punk", "Shoegaze", "Emo", "Industrial", "Noise", "Experimental", "Avant-Garde", "Minimalism", "Baroque", "Renaissance", "Medieval", "Fado", "Samba", "Bossa Nova", "Tango", "Flamenco", "Cumbia", "Salsa", "Merengue", "Reggaeton", "Afrobeat", "Highlife", "Soukous", "Zydeco"]

class GenreName:
    def __init__(self, name: str):
        if not isinstance(name, str) or len(name) < 0 or len(name) > 100:
            raise TypeError("Genre name must be a string of maximum 100 characters.")
        if name not in valid_genres:
            name = "Unknown"
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, GenreName):
            return self.name == other.name
        return False