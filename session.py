from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy import String
from databse import engine, async_engine
from typing import Annotated

async_session = async_sessionmaker(async_engine) # create session for work with BD
sync_session = sessionmaker(engine)


str_256 = Annotated[str, 256] # create annotate 

class Base(DeclarativeBase): # input annotation for classes which we use in models
    type_annotation_map = {
        str_256: String(256)
    }
