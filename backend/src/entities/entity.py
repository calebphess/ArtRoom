# coding=utf-8

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'artroomdb.c9ttkln8ouki.us-east-1.rds.amazonaws.com:3306'
db_name = 'artroomdb'
db_user = 'artroomadmin'
db_password = 'ArtR00m!'
engine = create_engine(f'mysql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Entity():
  id = Column(Integer, primary_key=True)
  created_at = Column(DateTime)
  updated_at = Column(DateTime)
  created_by = Column(Integer)
  last_updated_by = Column(Integer)

  def __init__(self, creator):
    self.created_at = datetime.now()
    self.updated_at = datetime.now()
    self.created_by = creator
    self.last_updated_by = creator
