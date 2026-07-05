from fastapi import FastAPI
from .GetVideogameRecord import get_videogame_record_by_id
from .CreateVideogameRecord import create_videogame_record, CreateVidegameRecordRequest
from .DeleteVideogameRecord import delete_videogame_record_by_id
from dotenv import load_dotenv
import os

load_dotenv()
mongo_url = os.getenv("MONGODB_URL")

app = FastAPI()

@app.get("/VideogamesRecords/get/{record_id}")
async def get_by_id(record_id):
    return get_videogame_record_by_id(record_id, mongo_url)

@app.post("/VideogamesRecords/create")
async def create_record(create_request: CreateVidegameRecordRequest):
    id = create_videogame_record(create_request, mongo_url)
    print(id)

@app.delete("/VideogamesRecords/delete/{record_id}")
async def delete_record(record_id):
    try:
        delete_videogame_record_by_id(record_id, mongo_url)
    except Exception as e:
        print(e)