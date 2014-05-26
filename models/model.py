
from datetime import datetime

import sqlalchemy
import sqlalchemy.ext.declarative

from sqlalchemy import Column, Sequence, Integer, String, Boolean, DateTime, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship, backref, relation



"""
from models.model import *
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
"""

class BaseBase(object):
  def toDict(self):
    model = {}
    for column in self.__table__.columns:
        model[column.name] = str(getattr(self, column.name))
    return model

Base = sqlalchemy.ext.declarative.declarative_base(cls=BaseBase)

class Image(Base):
  __tablename__ = 'image'
  id = Column(Integer, Sequence('image_id_seq'), primary_key=True)
  url = Column(String(256))

  created = Column(DateTime)
  modified = Column(DateTime)

  def __init__(self, url):
    self.url = url

    self.created = datetime.now()
    self.modified = datetime.now()



#url = 'mysql+mysqlconnector://altstars:o#fi3j0#(H0(j3q0f0#@koukilab.com/altstars'
url = 'sqlite:///:memory:'
engine = sqlalchemy.create_engine(url, encoding='utf8', echo=True)

