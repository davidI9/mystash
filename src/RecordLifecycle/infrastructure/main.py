from fastapi import FastAPI
from .Controllers.GetVideogameRecord import create_get_videogame_record_by_id_endpoint
from .Controllers.CreateVideogameRecord import create_videogame_record_endpoint
from .Controllers.DeleteVideogameRecord import delete_videogame_record_by_id_endpoint
from .Controllers.GetUserVideogameRecords import get_user_videogame_records_endpoint
from .Controllers.UpdateVideogameRecord import update_videogame_record, UpdateVideogameRecordRequest
from src.RecordLifecycle.application.UseCases.VideogameRecord.GetVideogameRecord.GetVideogameRecordHandler import GetVideogameRecordHandler
from src.RecordLifecycle.application.UseCases.VideogameRecord.CreateVideogameRecord.CreateVideogameRecordHandler import CreateVideogameRecordHandler
from src.RecordLifecycle.application.UseCases.VideogameRecord.DeleteVideogameRecord.DeleteVideogameRecordHandler import DeleteVideogameRecordHandler
from src.RecordLifecycle.application.UseCases.VideogameRecord.GetUserVideogameRecords.GetUserVideogameRecordsHandler import GetUserVideogameRecordsHandler
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

create_videogame_record_handler = CreateVideogameRecordHandler(repo)
create_videogame_record_router = create_videogame_record_endpoint(create_videogame_record_handler)

delete_videogame_record_handler = DeleteVideogameRecordHandler(repo)
delete_videogame_record_router = delete_videogame_record_by_id_endpoint(delete_videogame_record_handler)

get_user_videogame_records_handler = GetUserVideogameRecordsHandler(repo)
get_user_videogame_records_router = get_user_videogame_records_endpoint(get_user_videogame_records_handler)

app = FastAPI()
app.include_router(get_videogame_record_router)
app.include_router(create_videogame_record_router)
app.include_router(delete_videogame_record_router)
app.include_router(get_user_videogame_records_router)

@app.get("/VideogamesRecords/get_user_records/{author_id}")
async def get_user_records(author_id: str):
    try:
        records = get_user_videogame_records(author_id, repo)
        return records
    except Exception as e:
        print(e)
        
@app.post("/VideogamesRecords/update")
async def update_record(update_request: UpdateVideogameRecordRequest):
    try:
        id = update_videogame_record(update_request, repo)
        return {"id": id}
    except Exception as e:
        print(e)