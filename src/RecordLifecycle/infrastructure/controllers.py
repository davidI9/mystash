from typing import Any
from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from pymongo.database import Database

# VIDEOGAME RECORDS IMPORTS

from .Controllers.VideogameRecords.GetVideogameRecord import get_videogame_record_endpoint
from .Controllers.VideogameRecords.CreateVideogameRecord import create_videogame_record_endpoint
from .Controllers.VideogameRecords.DeleteVideogameRecord import delete_videogame_record_by_id_endpoint
from .Controllers.VideogameRecords.GetUserVideogameRecords import get_user_videogame_records_endpoint
from .Controllers.VideogameRecords.UpdateVideogameRecord import update_videogame_record_endpoint
from src.RecordLifecycle.application.UseCases.VideogameRecord.GetVideogameRecord.GetVideogameRecordHandler import GetVideogameRecordHandler
from src.RecordLifecycle.application.UseCases.VideogameRecord.CreateVideogameRecord.CreateVideogameRecordHandler import CreateVideogameRecordHandler
from src.RecordLifecycle.application.UseCases.VideogameRecord.DeleteVideogameRecord.DeleteVideogameRecordHandler import DeleteVideogameRecordHandler
from src.RecordLifecycle.application.UseCases.VideogameRecord.GetUserVideogameRecords.GetUserVideogameRecordsHandler import GetUserVideogameRecordsHandler
from src.RecordLifecycle.application.UseCases.VideogameRecord.UpdateVideogameRecord.UpdateVideogameRecordHandler import UpdateVideogameRecordHandler
from .Persistance.VideogameRecordRepositoryImpl import VideogameRecordRepositoryImpl

# SONG RECORDS IMPORTS

from .Controllers.SongRecords.GetSongRecord import get_song_record_endpoint
from .Controllers.SongRecords.CreateSongRecord import create_song_record_endpoint
from .Controllers.SongRecords.DeleteSongRecord import delete_song_record_endpoint
from .Controllers.SongRecords.GetUserSongRecords import get_user_song_records_endpoint
from .Controllers.SongRecords.UpdateSongRecord import update_song_record_endpoint
from src.RecordLifecycle.application.UseCases.SongRecord.GetSongRecord.GetSongRecordHandler import GetSongRecordHandler
from src.RecordLifecycle.application.UseCases.SongRecord.CreateSongRecord.CreateSongRecordHandler import CreateSongRecordHandler
from src.RecordLifecycle.application.UseCases.SongRecord.DeleteSongRecord.DeleteSongRecordHandler import DeleteSongRecordHandler
from src.RecordLifecycle.application.UseCases.SongRecord.GetUserSongRecords.GetUserSongRecordsHandler import GetUserSongRecordsHandler
from src.RecordLifecycle.application.UseCases.SongRecord.UpdateSongRecord.UpdateSongRecordHandler import UpdateSongRecordHandler
from .Persistance.SongRecordRepositoryImpl import SongRecordRepositoryImpl

# ALBUM RECORDS IMPORTS

from .Controllers.AlbumRecords.GetAlbumRecord import get_album_record_endpoint
from .Controllers.AlbumRecords.CreateAlbumRecord import create_album_record_endpoint
from .Controllers.AlbumRecords.DeleteAlbumRecord import delete_album_record_endpoint
from .Controllers.AlbumRecords.GetUserAlbumRecords import get_user_album_records_endpoint
from .Controllers.AlbumRecords.UpdateAlbumRecord import update_album_record_endpoint
from src.RecordLifecycle.application.UseCases.AlbumRecord.GetAlbumRecord.GetAlbumRecordHandler import GetAlbumRecordHandler
from src.RecordLifecycle.application.UseCases.AlbumRecord.CreateAlbumRecord.CreateAlbumRecordHandler import CreateAlbumRecordHandler
from src.RecordLifecycle.application.UseCases.AlbumRecord.DeleteAlbumRecord.DeleteAlbumRecordHandler import DeleteAlbumRecordHandler
from src.RecordLifecycle.application.UseCases.AlbumRecord.GetUserAlbumRecords.GetUserAlbumRecordsHandler import GetUserAlbumRecordsHandler
from src.RecordLifecycle.application.UseCases.AlbumRecord.UpdateAlbumRecord.UpdateAlbumRecordHandler import UpdateAlbumRecordHandler
from .Persistance.AlbumRecordRepositoryImpl import AlbumRecordRepositoryImpl

###########################
# VIDEOGAME RECORDS ROUTES
###########################

def setup_videogame_record_router(videogame_repo: VideogameRecordRepositoryImpl) -> APIRouter:
    
    get_videogame_record_handler = GetVideogameRecordHandler(videogame_repo)
    get_videogame_record_router = get_videogame_record_endpoint(get_videogame_record_handler)

    create_videogame_record_handler = CreateVideogameRecordHandler(videogame_repo)
    create_videogame_record_router = create_videogame_record_endpoint(create_videogame_record_handler)

    delete_videogame_record_handler = DeleteVideogameRecordHandler(videogame_repo)
    delete_videogame_record_router = delete_videogame_record_by_id_endpoint(delete_videogame_record_handler)

    get_user_videogame_records_handler = GetUserVideogameRecordsHandler(videogame_repo)
    get_user_videogame_records_router = get_user_videogame_records_endpoint(get_user_videogame_records_handler)

    update_videogame_record_handler = UpdateVideogameRecordHandler(videogame_repo)
    update_videogame_record_router = update_videogame_record_endpoint(update_videogame_record_handler)

    videogame_record_router = APIRouter(prefix="/VideogamesRecords", tags=["VideogamesRecordsRoutes"])
    videogame_record_router.include_router(get_videogame_record_router)
    videogame_record_router.include_router(create_videogame_record_router)
    videogame_record_router.include_router(delete_videogame_record_router)
    videogame_record_router.include_router(get_user_videogame_records_router)
    videogame_record_router.include_router(update_videogame_record_router)

    return videogame_record_router

###########################
# SONG RECORDS ROUTES
###########################

def setup_song_record_router(song_repo: SongRecordRepositoryImpl) -> APIRouter:

    get_song_record_handler = GetSongRecordHandler(song_repo)
    get_song_record_router = get_song_record_endpoint(get_song_record_handler)

    create_song_record_handler = CreateSongRecordHandler(song_repo)
    create_song_record_router = create_song_record_endpoint(create_song_record_handler)

    delete_song_record_handler = DeleteSongRecordHandler(song_repo)
    delete_song_record_router = delete_song_record_endpoint(delete_song_record_handler)

    get_user_song_records_handler = GetUserSongRecordsHandler(song_repo)
    get_user_song_records_router = get_user_song_records_endpoint(get_user_song_records_handler)

    update_song_record_handler = UpdateSongRecordHandler(song_repo)
    update_song_record_router = update_song_record_endpoint(update_song_record_handler)

    song_record_router = APIRouter(prefix="/SongRecords", tags=["SongRecordsRoutes"])
    song_record_router.include_router(get_song_record_router)
    song_record_router.include_router(create_song_record_router)
    song_record_router.include_router(delete_song_record_router)
    song_record_router.include_router(get_user_song_records_router)
    song_record_router.include_router(update_song_record_router)

    return song_record_router

###########################
# ALBUM RECORDS ROUTES
###########################

def setup_album_record_router(album_repo: AlbumRecordRepositoryImpl, song_repo: SongRecordRepositoryImpl) -> APIRouter:
    
    get_album_record_handler = GetAlbumRecordHandler(album_repo, song_repo)
    get_album_record_router = get_album_record_endpoint(get_album_record_handler)
    
    create_album_record_handler = CreateAlbumRecordHandler(album_repo)
    create_album_record_router = create_album_record_endpoint(create_album_record_handler)
    
    delete_album_record_handler = DeleteAlbumRecordHandler(album_repo)
    delete_album_record_router = delete_album_record_endpoint(delete_album_record_handler)
    
    get_user_album_records_handler = GetUserAlbumRecordsHandler(album_repo, song_repo)
    get_user_album_records_router = get_user_album_records_endpoint(get_user_album_records_handler)
    
    update_album_record_handler = UpdateAlbumRecordHandler(album_repo)
    update_album_record_router = update_album_record_endpoint(update_album_record_handler)
    
    album_record_router = APIRouter(prefix="/AlbumRecords", tags=["AlbumRecordsRoutes"])
    album_record_router.include_router(get_album_record_router)
    album_record_router.include_router(create_album_record_router)
    album_record_router.include_router(delete_album_record_router)
    album_record_router.include_router(get_user_album_records_router)
    album_record_router.include_router(update_album_record_router)
    
    return album_record_router

def get_record_router(mongo_client: MongoClient) -> APIRouter:
    
    videogame_database: Database[dict[str, Any]]
    song_database: Database[dict[str, Any]]
    album_database: Database[dict[str, Any]]
    
    videogame_database = mongo_client["base_de_datos"]
    videogame_repo = VideogameRecordRepositoryImpl(videogame_database)
    videogame_record_router = setup_videogame_record_router(videogame_repo)
    
    song_database = mongo_client["song_database"]
    song_repo = SongRecordRepositoryImpl(song_database)
    song_record_router = setup_song_record_router(song_repo)
    
    album_database = mongo_client["album_database"]
    album_repo = AlbumRecordRepositoryImpl(album_database)
    album_record_router = setup_album_record_router(album_repo, song_repo)

    record_router = APIRouter(prefix="/Records", tags=["RecordsRoutes"])
    
    record_router.include_router(videogame_record_router)
    record_router.include_router(song_record_router)
    record_router.include_router(album_record_router)

    return record_router