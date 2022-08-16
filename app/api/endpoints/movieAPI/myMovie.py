
# import the required packages.
from typing import List, Tuple, Union
from fastapi import Depends, APIRouter


from app.database.fakeDB.fakeDb import fake_movie_db
from app.pydanticModel.models import  Movie
from app.main import get_db


from sqlalchemy.orm import Session
# from app.middleware.functions import getMovieList


#You can think of APIRouter as a "mini FastAPI" class.
myMovies = APIRouter()

@myMovies.get('/records', response_model=Movie)
def show_records(db: Session = Depends(get_db)):
    records = db.query(Movie).all()
    return records