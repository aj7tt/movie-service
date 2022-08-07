#~/movie-service/app/api/movies.py

from typing import List, Union, Tuple
from fastapi import Header, APIRouter,HTTPException

from app.api.models import Movie, CreateUser
from app.database.db import fake_movie_db

#You can think of APIRouter as a "mini FastAPI" class.
movies = APIRouter()

@movies.get('/', response_model=List[Movie])
async def index():
    return fake_movie_db

# @movies.get('/{id}', response_model=List[Movie])
# async def getMovieById(id):
#     id = int(id)
#     if 'id' not in fake_movie_db:
#         raise HTTPException('Movie Id no : {} not found'.format(id))
#     return fake_movie_db[id]

@movies.post('/add', status_code=201)
async def add_movie(payload: Movie):
    movie = payload.dict()
    fake_movie_db.append(movie)
    return {'The length of db is now ': len(fake_movie_db) - 1}

@movies.put('/{id}')
async def update_movie(id: int, payload: Movie):
    movie = payload.dict()
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        fake_movie_db[id] = movie
        return None
    raise HTTPException(status_code=404, detail="Movie with given id not found")

@movies.delete('/{id}')
async def delete_movie(id: int):
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        del fake_movie_db[id]
        return None
    raise HTTPException(status_code=404, detail="Movie with given id not found")