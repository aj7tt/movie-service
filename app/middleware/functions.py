
from app.database.schema.movieDataSchema import movieList
from app.database.dbConfig.config import db

from app.pydanticModel.models import movie
async def getMovieList():
    query = movie.select()
    return await db.fetch_all(query=query)