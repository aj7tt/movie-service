
# import the required packages.
from fastapi import Depends, APIRouter
from app.database.dbConfig.config import SessionLocal, get_db

from app.pydanticModel.models import Movie




# from app.middleware.functions import getMovieList


#You can think of APIRouter as a "mini FastAPI" class.
myMovies = APIRouter()

@myMovies.get('/records', response_model=Movie)
def show_records(db: SessionLocal = Depends(get_db)):
    records = db.query(Movie).all()
    return records


@myMovies.get('/movie')
def health():
    return {'ok'}