#~/movie-service/api/models.py

import time 
from datetime import datetime
from enum import Enum
from uuid import UUID
from typing import List,Union,  Optional
from pydantic import BaseModel, validator, root_validator

'''
#declare the request data model

'''

#inherit from BaseModel class of Pydantic
class Movie(BaseModel):
    """
    This is the description of the Movie model
    """

    id :  int
    name: str 
    plot: str 
    genres: List[str]
    casts: List[str]
    Industry = Enum("Bollywood", 'Hollywood') 
    #Accepting optional values
    Gross: Optional[str]=None


    class Config:
        orm_mode = True


    

    
    #validation for id (only SuperUser can delete this)
    # @validator("id")
    # def ValidateId(cls, value):
    #     if "delete from" in value:
    #         raise ValueError("you cannot delete an existing id")
    #     return value
    
    #validation for name , title of movie
    # @validator('title', check_fields=False)
    # def validateName(cls, value):
    #     assert value.isalnum() or value.isspace() , 'must be alphanumeric and space only'
    #     return value

    # #validation for Plot
    # @validator('plot')
    # def validatePlot(cls, space):
    #     if ' ' not in space:
    #         raise ValueError('must contain a space')
    #     return space.title()

#user details 
# class CreateUser(BaseModel):
    """
    This is the description of user
    """
    name : str
    email : str
    password :str 
    confirm_password :str 

    @root_validator()
    def verify_password_match(cls,values):
        password = values.get("password")
        confirm_password = values.get("confirm_password")

        if password != confirm_password:
            raise ValueError("The two passwords did not match.")
        return values