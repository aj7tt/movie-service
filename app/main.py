#~/movie-service/app/main.py

# FastAPI is a Python class that provides all the functionality for the API.
from fastapi import FastAPI
from starlette.responses import RedirectResponse
#config file
from app.core.config import Settings
from .api.Api import router as apiRouter
from app.api.endpoints.fakeMovieAPI.movieApi import movies
from .database.dbConfig.config import SessionLocal



# app is instance of the class FastAPI 
app = FastAPI(title=Settings.PROJECT_NAME,version=Settings.PROJECT_VERSION)


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


#default root
@app.get("/testApp")
async def root():
    return{
        "Status_code: 2000K! "
    }

#router for different api
app.include_router(apiRouter)
