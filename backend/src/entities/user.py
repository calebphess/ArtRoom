# coding=utf-8

from sqlalchemy import Column, String
from .entity import Entity, Base

class User(Entity, Base):
  __tablename__ = 'users'

  first_name = Column(String(32), nullable=False)
  last_name = Column(String(32))
  username = Column(String(64), unique=True)

  def __init__(self, first_name, last_name, username, creator):
    Entity.__init__(self, creator)
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
