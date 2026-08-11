from fastapi import FastAPI
from pymongo import MongoClient
import os
from src.RecordLifecycle.infrastructure.records_controllers import get_record_router

app = FastAPI()
mongo_client : MongoClient = MongoClient(os.getenv("MONGODB_URL"))
app.include_router(get_record_router(mongo_client))