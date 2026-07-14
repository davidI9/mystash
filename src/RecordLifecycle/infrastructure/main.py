from fastapi import FastAPI
from .Controllers.GetVideogameRecord import get_videogame_record_by_id
from .Controllers.CreateVideogameRecord import create_videogame_record, CreateVidegameRecordRequest
from .Controllers.DeleteVideogameRecord import delete_videogame_record_by_id
from .Controllers.GetUserVideogameRecords import get_user_videogame_records
from .Controllers.UpdateVideogameRecord import update_videogame_record, UpdateVideogameRecordRequest
from .Persistance.VideogameMongodbRepo import VideogameMongodbRepo
from .Persistance.VideogameRecordRepositoryImpl import VideogameRecordRepositoryImpl
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()
mongo_url = os.getenv("MONGODB_URL")
database = (MongoClient(mongo_url))["base_de_datos"]

repo = VideogameRecordRepositoryImpl(VideogameMongodbRepo(database))

app = FastAPI()

@app.get("/VideogamesRecords/get/{record_id}")
async def get_by_id(record_id: str):
    try:
        record = get_videogame_record_by_id(record_id, repo)
        return record
    except Exception as e:
        print(e)

@app.get("/VideogamesRecords/get_user_records/{author_id}")
async def get_user_records(author_id: str):
    try:
        records = get_user_videogame_records(author_id, repo)
        return records
    except Exception as e:
        print(e)

@app.post("/VideogamesRecords/create")
async def create_record(create_request: CreateVidegameRecordRequest):
    try:
        id = create_videogame_record(create_request, repo)
        return {"id": id}
    except Exception as e:
        print(e)

@app.delete("/VideogamesRecords/delete/{record_id}")
async def delete_record(record_id: str):
    try:
        delete_videogame_record_by_id(record_id, repo)
    except Exception as e:
        print(e)
        
@app.post("/VideogamesRecords/update")
async def update_record(update_request: UpdateVideogameRecordRequest):
    try:
        id = update_videogame_record(update_request, repo)
        return {"id": id}
    except Exception as e:
        print(e)