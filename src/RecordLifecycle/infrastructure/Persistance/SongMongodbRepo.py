from src.RecordLifecycle.domain.Entities.SongRecord import SongRecord
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from pymongo.database import Database
from pymongo.cursor import Cursor
from typing import Any

class SongMongodbRepo:
    def __init__(self, database: Database):
        self.song_records = database["song_records"]
    
    def save_in_db(self, record: SongRecord):
        try:
            self.song_records.insert_one({
                "author_id": str(record.get_author()),
                "record_id": str(record.get_id()),
                "title": str(record.get_title()),
                "date": str(record.get_date()),
                "artist": str(record.get_artist()),
                "main_genre": str(record.get_main_genre()),
                "duration": str(record.get_duration()),
                "album_id": str(record.get_album()) if record.get_album() else None
            })
        except Exception as e:
            print(f"An error has occurred while saving in MongoDB: {e}")
    
    def get_by_id_from_db(self, id: RecordId):
        raw_record: dict[str, Any] | None
        record: SongRecord | None
        
        try:
            raw_record = self.song_records.find_one({"record_id": str(id)})
            record = self.map_record(raw_record)
            return record
        
        except Exception as e:
            print("An error has ocurred while getting the requested record from MongoDB.")
    
    def map_record(self, raw_record):
        record = SongRecord(raw_record["author_id"], raw_record["title"], raw_record["date"], raw_record["record_id"], raw_record["artist"], raw_record["main_genre"], raw_record["duration"], raw_record["album_id"])
        return record
    
    def delete_by_id(self, id: RecordId):
        try:
            self.song_records.delete_one({"record_id": str(id)})
            print("Deleted without errors.")
        except Exception as e:
            print(f"An error has occurred while deleting from MongoDB: {e}")
            
    def get_user_records(self, author_id: AuthorId):
        raw_records: Cursor

        try:
            raw_records = self.song_records.find({"author_id": str(author_id)})
            records = [self.map_record(raw_record) for raw_record in raw_records]
            return records
        except Exception as e:
            print(f"An error has occurred while getting user records from MongoDB: {e}")
            
    def update_record(self, record: SongRecord):
        try:
            self.song_records.update_one(
                {"record_id": str(record.get_id())},
                {"$set": {
                    "title": str(record.get_title()),
                    "date": str(record.get_date()),
                    "artist": str(record.get_artist()),
                    "main_genre": str(record.get_main_genre()),
                    "duration": str(record.get_duration()),
                    "album_id": str(record.get_album()) if record.get_album() else None
                }}
            )
            print("Updated without errors.")
        except Exception as e:
            print(f"An error has occurred while updating in MongoDB: {e}")
    
    def get_album_songs(self, album_id: RecordId):
        raw_records: Cursor

        try:
            raw_records = self.song_records.find({"album_id": str(album_id)})
            records = [self.map_record(raw_record) for raw_record in raw_records]
            return records
        except Exception as e:
            print(f"An error has occurred while getting album records from MongoDB: {e}")