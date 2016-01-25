#!/usr/bin/env python3
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

# connect to database
engine = create_engine(
    'mysql+mysqlconnector://user:password@127.0.0.1:3306/test',
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


# create a Session object
Session = sessionmaker(bind=engine)

# instantiate a Session
session = Session()



# create a test row called ed_user
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')

# add it into session
session.add(ed_user)

# we can create and add more rows at once use session.add_all
session.add_all([
User(name='wendy', fullname='Wendy Williams', password='foobar'),
User(name='mary', fullname='Mary Contrary', password='xxg527'),
User(name='fred', fullname='Fred Flinstone', password='blah')])

# we also can change something...
ed_user.password = 'f8s7ccs'

# now let's commit
session.commit()
