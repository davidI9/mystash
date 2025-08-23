class VideogameRating:
    def __init__(self, rating):
        if not isinstance(rating, (int, float)):
            raise TypeError("Rating should be either an int or a float")
            
        if rating >=0 and rating <=10:
            self._rating = rating
            
        else:
            raise ValueError("Rating must be a number between 0 and 10.")

    
    def __repr__(self):
        return float(self._rating)
    
    def __eq__(self, value):
        return isinstance(value, VideogameRating) and self._rating == value._rating
    
    def __float__(self):
        return float(self._rating)