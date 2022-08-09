

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#file config
from app.database.dbConfig.config import Base


# Create the database models

class User(Base):
    __tablename__ = "users"

    userid = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    movie = relationship("Item", back_populates="owner")

class movieList(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    plot = Column(String(255))
    indstry = Column(String(255))
    genres = Column(String(255))
    casts = Column(String(255))
    Gross = Column(String(255))
    owner_id = Column(Integer, ForeignKey("users.userid"))

    owner = relationship("User", back_populates="movie")
