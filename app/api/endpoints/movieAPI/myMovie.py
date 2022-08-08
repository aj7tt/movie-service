
# import the required packages.
from typing import List, Tuple, Union

from app.database.fakeDB.fakeDb import fake_movie_db
from app.pydanticModel.models import CreateUser, Movie
from fastapi import APIRouter, Header, HTTPException

from app.middleware.functions import getMovieList


#You can think of APIRouter as a "mini FastAPI" class.
myMovies = APIRouter()

@myMovies.get('/', response_model=List[Movie])
async def home():
    return {getMovieList()}