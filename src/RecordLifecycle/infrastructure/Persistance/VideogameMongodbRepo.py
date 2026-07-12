from pymongo import MongoClient
from src.RecordLifecycle.domain.Entities.VideogameRecord import VideogameRecord
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId

class VideogameMongodbRepo:
        def __init__(self, connection_url: str):
            database = (MongoClient(connection_url))["base_de_datos"]
            self.videogame_records = database["videogame_records"]
        
        def save_in_db(self, record: VideogameRecord):
            try:    
                self.videogame_records.insert_one({
                    "author_id": str(record.get_author()),
                    "record_id": str(record.get_id()),
                    "title": str(record.get_title()),
                    "description": str(record.get_description()),
                    "creation_date": str(record.get_date()),
                    "rating": float(record.get_rating()),
                    "playtime": int(record.get_playtime()),
                })
            
            except Exception as e:
                print(f"An error has occurred while saving in MongoDB: {e}")
        
        def get_by_id_from_db(self, id: RecordId):
            try:
                raw_record = self.videogame_records.find_one({"record_id": str(id)})
                record = self.map_record(raw_record)
                return record
            
            except Exception as e:
                print("An error has ocurred while getting the requested record from MongoDB.")
        
        def map_record(self, raw_record):
            record = VideogameRecord(raw_record["author_id"], raw_record["title"], raw_record["creation_date"], raw_record["record_id"], raw_record["description"], raw_record["rating"], raw_record["playtime"])
            return record
        
        def delete_by_id(self, id: RecordId):
            try:
                self.videogame_records.delete_one({"record_id": str(id)})
                print("Deleted without errors.")
            except Exception as e:
                print(e)
                
        def get_user_records(self, author_id: AuthorId):
            try:
                raw_records = self.videogame_records.find({"author_id": str(author_id)})
                records = [self.map_record(raw_record) for raw_record in raw_records]
                return records
            except Exception as e:
                print(e)
                
        def update_record(self, record: VideogameRecord):
            try:
                self.videogame_records.update_one(
                    {"record_id": str(record.get_id()), "author_id": str(record.get_author())},
                    {"$set": {
                        "title": str(record.get_title()),
                        "description": str(record.get_description()),
                        "creation_date": str(record.get_date()),
                        "rating": float(record.get_rating()),
                        "playtime": int(record.get_playtime())
                    }}
                )
                print("Record updated successfully.")
            except Exception as e:
                print(f"An error has occurred while updating the record in MongoDB: {e}")