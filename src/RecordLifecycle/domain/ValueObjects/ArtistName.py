class ArtistName:
    def __init__(self, name: str):
        if not isinstance(name, str) or len(name) < 0 or len(name) > 100:
            raise TypeError("The name must be a string of maximum 100 characters.")
        if(len(name) == 0):
            name = "Unknown"
        self.name = name

    def __str__(self):
        return self.name
    
    def __eq__(self, value):
        return isinstance(value, ArtistName) and self.name == value.name
    
    def __repr__(self):
        return str(self.name)