#~/movie-service/app/main.py

# FastAPI is a Python class that provides all the functionality for the API.
from fastapi import FastAPI
import uvicorn
from app.core.config import Settings
from .api.Api import router as apiRouter
from app.api.endpoints.fakeMovieAPI.movieApi import movies



# app is instance of the class FastAPI 
app = FastAPI(title=Settings.PROJECT_NAME,version=Settings.PROJECT_VERSION)



#router for different api
app.include_router(apiRouter)


#default root
@app.get("/")
async def root():
    return{
        "Status_code: 2000K! "
    }


# if __name__ == "__main__":
#     uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)