#~/movie-service/app/main.py

# FastAPI is a Python class that provides all the functionality for the API.
from fastapi import FastAPI

from app.api.endpoints import movies
from app.core.config import Settings
import uvicorn

# app is instance of the class FastAPI 
app = FastAPI(title=Settings.PROJECT_NAME,version=Settings.PROJECT_VERSION)

app.include_router(movies)


# if __name__ == "__main__":
#     uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)