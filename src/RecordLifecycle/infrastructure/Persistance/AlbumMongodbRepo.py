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
            
            
        def get_by_id_from_db(self, id: RecordId):
            raw_record: dict[str, Any] | None
            record: AlbumRecord | None
            
            try:
                raw_record = self.album_records.find_one({"record_id": str(id)})
                record = self.map_record(raw_record)
                return record
            
            except Exception as e:
                print("An error has ocurred while getting the requested record from MongoDB.")
                
        def map_record(self, raw_record):
            record = AlbumRecord(raw_record["author_id"], raw_record["title"], raw_record["date"], raw_record["record_id"], raw_record["artist"], raw_record["main_genre"])
            return record
        
        def delete_by_id(self, id: RecordId):
            try:
                self.album_records.delete_one({"record_id": str(id)})
                print("Deleted without errors.")
            except Exception as e:
                print(e)
        
        def get_user_records(self, author_id: AuthorId):
            raw_records: Cursor

            try:
                raw_records = self.album_records.find({"author_id": str(author_id)})
                records = [self.map_record(raw_record) for raw_record in raw_records]
                return records
            except Exception as e:
                print(e)
                
        def update_record(self, record: AlbumRecord):
            try:
                self.album_records.update_one(
                    {"record_id": str(record.get_id()), "author_id": str(record.get_author())},
                    {"$set": {
                        "title": str(record.get_album_title()),
                        "date": str(record.get_date()),
                        "artist": str(record.get_artist()),
                        "main_genre": str(record.get_main_genre())
                    }}
                )
                print("Updated without errors.")
            except Exception as e:
                print(e)