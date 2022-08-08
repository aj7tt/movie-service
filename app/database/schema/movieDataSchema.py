
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                         ARRAY, CHAR, VARCHAR)

from app.database.dbConfig.config import db
from sqlalchemy.dialects.postgresql import JSON


class movieList(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True),
    name = db.Column(db.String(50)),
    plot = db.Column(db.String(255)),
    indstry = db.Column(db.String(255)),
    genres = db.Column(db.String(255)),
    casts = db.Column(db.String(255)),
    Gross = db.Column(db.String(255))
