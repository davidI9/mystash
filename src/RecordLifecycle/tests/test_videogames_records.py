from ..domain.VideogameRecord import VideogameRecord
from ..domain.ValueObjects import RecordTitle, CreationDate, VideogameDescription, VideogameRating, VideogamePlaytime, RecordId

def test_videogames_records():
    #arrange
        id = RecordId()
        author = "550e8400-e29b-41d4-a716-446655440002"
        title = RecordTitle("Test Record")
        date = CreationDate("11/06/2006")
        description = VideogameDescription("test description")
        rating = VideogameRating(3)
        playtime = VideogamePlaytime(127)
        record = VideogameRecord(author, title, date, id,  description, rating, playtime)
        
    #act
        try:
            record.set_date("01/06/2007")
            record.set_date("ginger")
        except (TypeError, ValueError):
            pass
        
    #assert
        assert(record.get_author() == "550e8400-e29b-41d4-a716-446655440002" )
        assert(record.get_date() == CreationDate('11/06/2006'))
        assert(record.get_rating() == VideogameRating(3))
        assert(record.get_title() == RecordTitle("Test Record"))