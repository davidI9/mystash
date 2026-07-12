from fastapi import FastAPI
from .GetVideogameRecord import get_videogame_record_by_id
from .CreateVideogameRecord import create_videogame_record, CreateVidegameRecordRequest
from .DeleteVideogameRecord import delete_videogame_record_by_id
from .GetUserVideogameRecords import get_user_videogame_records
from .UpdateVideogameRecord import update_videogame_record, UpdateVideogameRecordRequest
from dotenv import load_dotenv
import os

load_dotenv()
mongo_url = os.getenv("MONGODB_URL")

app = FastAPI()

@app.get("/VideogamesRecords/get/{record_id}")
async def get_by_id(record_id: str):
    try:
        record = get_videogame_record_by_id(record_id, mongo_url)
        return record
    except Exception as e:
        print(e)

@app.get("/VideogamesRecords/get_user_records/{author_id}")
async def get_user_records(author_id: str):
    try:
        records = get_user_videogame_records(author_id, mongo_url)
        return records
    except Exception as e:
        print(e)

@app.post("/VideogamesRecords/create")
async def create_record(create_request: CreateVidegameRecordRequest):
    try:
        id = create_videogame_record(create_request, mongo_url)
        return {"id": id}
    except Exception as e:
        print(e)

@app.delete("/VideogamesRecords/delete/{record_id}")
async def delete_record(record_id: str):
    try:
        delete_videogame_record_by_id(record_id, mongo_url)
    except Exception as e:
        print(e)
        
@app.post("/VideogamesRecords/update")
async def update_record(update_request: UpdateVideogameRecordRequest):
    try:
        id = update_videogame_record(update_request, mongo_url)
        return {"id": id}
    except Exception as e:
        print(e)