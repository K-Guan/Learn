#!/usr/bin/env python3
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

# connect to database
engine = create_engine(
    'mysql+mysqlconnector://username:password@127.0.0.1:3306/test',
     echo=True)

# create a base Table obejct
Base = declarative_base()


# create a Table object called User
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    fullname = Column(Text, nullable=True)

# create the table in database
Base.metadata.create_all(engine)
