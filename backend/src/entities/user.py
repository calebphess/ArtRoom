# coding=utf-8

from sqlalchemy import Column, String
from marshmallow import Schema, fields
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

class UserSchema(Schema):
  id = fields.Number()
  first_name = fields.Str()
  last_name = fields.Str()
  username = fields.Str()
  created_at = fields.DateTime()
  updated_at = fields.DateTime()
  last_updated_by = fields.Int()
  created_by = fields.Int()
