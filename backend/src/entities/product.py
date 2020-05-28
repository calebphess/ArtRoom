# coding=utf-8

from sqlalchemy import Column, String, Float
from marshmallow import Schema, fields
from .entity import Entity, Base

class Product(Entity, Base):
  __tablename__ = 'products'

  name = Column(String(32), nullable=False)
  description = Column(String(255))
  image_url = Column(String(255), unique=True, nullable=False)
  price = Column(Float, nullable=False)

  def __init__(self, name, description, image_url, price, creator):
    Entity.__init__(self, creator)
    self.name = name
    self.description = description
    self.image_url = image_url
    self.price = price

class ProductSchema(Schema):
  id = fields.Number()
  name = fields.Str()
  description = fields.Str()
  image_url = fields.Str()
  price = fields.Float()
  created_at = fields.DateTime()
  updated_at = fields.DateTime()
  last_updated_by = fields.Int()
  created_by = fields.Int()
