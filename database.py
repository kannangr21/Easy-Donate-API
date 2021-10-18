import os
import re

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config
uri = config("DATABASE_URL")
if uri.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = uri.replace("postgres://", "postgresql://", 1)
else:
    SQLALCHEMY_DATABASE_URL = uri
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()