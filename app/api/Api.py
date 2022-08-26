#~/movie-service/app/api/api.py

from fastapi import APIRouter 

router = APIRouter()


from .endpoints.fakeMovieAPI.movieApi import movies as fakeMovieAPIRouter
# router for fake movie api service
router.include_router(fakeMovieAPIRouter)

# route for movie api service
from .endpoints.movieAPI.myMovie import myMovies as movieAPIRouter
router.include_router(movieAPIRouter)



