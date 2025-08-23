from fastapi import FastAPI
from .GetVideogameRecord import get_videogame_record_by_id
from .CreateVideogameRecord import create_videogame_record, CreateVidegameRecordRequest
from .DeleteVideogameRecord import delete_videogame_record_by_id

app = FastAPI()

@app.get("/VideogamesRecords/get/{record_id}")
async def get_by_id(record_id):
    return get_videogame_record_by_id(record_id)

@app.post("/VideogamesRecords/create")
async def create_record(create_request: CreateVidegameRecordRequest):
    id = create_videogame_record(create_request)
    print(id)

@app.delete("/VideogamesRecords/delete/{record_id}")
async def delete_record(record_id):
    try:
        delete_videogame_record_by_id(record_id)
    except Exception as e:
        print(e)