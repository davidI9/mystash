from src.RecordLifecycle.domain.Entities.VideogameRecord import VideogameRecord
from src.RecordLifecycle.domain.ValueObjects import RecordTitle
from src.RecordLifecycle.domain.ValueObjects import CreationDate
from src.RecordLifecycle.domain.ValueObjects import VideogameDescription
from src.RecordLifecycle.domain.ValueObjects import VideogameRating
from src.RecordLifecycle.domain.ValueObjects import VideogamePlaytime
from src.RecordLifecycle.domain.ValueObjects import RecordId
from src.RecordLifecycle.domain.ValueObjects import AuthorId

def test_videogames_records():
    #arrange
        id = RecordId("550e8400-e29b-41d4-a716-446655440002")
        author = AuthorId("550e8400-e29b-41d4-a716-446655440012")
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
        assert(record.get_id() == RecordId("550e8400-e29b-41d4-a716-446655440002"))
        assert(record.get_author() == AuthorId("550e8400-e29b-41d4-a716-446655440012"))
        assert(record.get_date() == CreationDate('11/06/2006'))
        assert(record.get_rating() == VideogameRating(3))
        assert(record.get_title() == RecordTitle("Test Record"))
        assert(record.get_description() == VideogameDescription("test description"))
        assert(record.get_playtime() == VideogamePlaytime(127))