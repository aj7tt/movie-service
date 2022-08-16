#~/movie-service/app/api/movies.py

# import the required packages.
from typing import List, Tuple, Union,Dict

from app.database.fakeDB.fakeDb import fake_movie_db
from app.pydanticModel.models import  Movie
from fastapi import APIRouter, Header, HTTPException

#You can think of APIRouter as a "mini FastAPI" class.
movies = APIRouter()

@movies.get('/movieList', response_model=Movie)
async def index():
    return fake_movie_db

@movies.get('/{id}', response_model=Movie)
async def getMovieById(id = int):
    id = int(id)
    if 'id' not in fake_movie_db:
        raise HTTPException('Movie Id no : {} not found'.format(id))
    return (fake_movie_db[1])

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
