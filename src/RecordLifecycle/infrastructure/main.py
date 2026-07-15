from fastapi import FastAPI
from .Controllers.GetVideogameRecord import create_get_videogame_record_by_id_endpoint
from .Controllers.CreateVideogameRecord import create_videogame_record, CreateVidegameRecordRequest
from .Controllers.DeleteVideogameRecord import delete_videogame_record_by_id
from .Controllers.GetUserVideogameRecords import get_user_videogame_records
from .Controllers.UpdateVideogameRecord import update_videogame_record, UpdateVideogameRecordRequest
from src.RecordLifecycle.application.UseCases.VideogameRecord.GetVideogameRecord.GetVideogameRecordHandler import GetVideogameRecordHandler
from .Persistance.VideogameRecordRepositoryImpl import VideogameRecordRepositoryImpl
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from pymongo.database import Database

client: MongoClient
database: Database

load_dotenv()

mongo_url = os.getenv("MONGODB_URL")
client = MongoClient(mongo_url)
database = client["base_de_datos"]

repo = VideogameRecordRepositoryImpl(database)
    
get_videogame_record_handler = GetVideogameRecordHandler(repo)

get_videogame_record_router = create_get_videogame_record_by_id_endpoint(get_videogame_record_handler)

app = FastAPI()
app.include_router(get_videogame_record_router)

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