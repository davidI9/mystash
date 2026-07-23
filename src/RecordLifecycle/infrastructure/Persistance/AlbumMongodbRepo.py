from src.RecordLifecycle.domain.Entities.AlbumRecord import AlbumRecord
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from pymongo.database import Database
from pymongo.cursor import Cursor
from typing import Any

class AlbumMongodbRepo:
        def __init__(self, database: Database):
            self.album_records = database["album_records"]
        
        def save_in_db(self, record: AlbumRecord):
            try:    
                self.album_records.insert_one({
                    "author_id": str(record.get_author()),
                    "record_id": str(record.get_id()),
                    "title": str(record.get_album_title()),
                    "date": str(record.get_date()),
                    "artist": str(record.get_artist()),
                    "main_genre": str(record.get_main_genre()),
                })
            except Exception as e:
                print(f"An error has occurred while saving in MongoDB: {e}")
            
            