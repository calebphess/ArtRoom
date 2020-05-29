# coding=utf-8
from flask_cors import CORS
from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.user import User, UserSchema
from .entities.product import Product, ProductSchema
from .auth import AuthError, requires_auth

# creating the flask application
app = Flask(__name__)
CORS(app)

# generate database schema
Base.metadata.create_all(engine)

# class for the /users endpoint
@app.route('/users')
def get_users():
  # start the database connection session
  session = Session()

  # fetching all users from the database
  user_objects = session.query(User).all()

  # transform the data to objects that can be serialized to JSON
  schema = UserSchema(many=True)
  users = schema.dump(user_objects)

  # close the session before we return
  session.close()

  # serialize as JSON and return
  return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
  # mount the user object
  posted_user = UserSchema(only=('first_name', 'last_name', 'username')).load(request.get_json())
  user = User(**posted_user, creator=0)

  # persist the user
  session = Session()
  session.add(user)
  session.commit()

  # return the created user
  new_user = UserSchema().dump(user)
  session.close()
  return jsonify(new_user), 201

# class for the /products endpoint
@app.route('/products')
def get_products():
  # start the database connection session
  session = Session()

  # fetching all products from the database
  product_objects = session.query(Product).all()

  # transform the data to objects that can be serialized to JSON
  schema = ProductSchema(many=True)
  products = schema.dump(product_objects)

  # close the session before we return
  session.close()

  # serialize as JSON and return
  return jsonify(products)

  
@app.route('/products', methods=['POST'])
@requires_auth
def add_product():
  # mount the product object
  posted_product = ProductSchema(only=('name', 'description', 'image_url', 'price')).load(request.get_json())
  product = Product(**posted_product, creator=0)

  # persist the product
  session = Session()
  session.add(product)
  session.commit()

  # return the created product
  new_product = ProductSchema().dump(product)
  session.close()
  return jsonify(new_product), 201

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

# start session
session = Session()

# check for existing user data
users = session.query(User).all()

if len(users) == 0:
  # create and persist dummy user
  dummy_user = User("Caleb", "Penn", "cpenn", 0)
  session.add(dummy_user)
  session.commit()
  session.close()

  # reload users
  users = session.query(User).all()

# check for existing product data
products = session.query(Product).all()

if len(products) == 0:
  # create and persist dummy product
  dummy_product = Product("Starry Night", "A graphic of a stary night", "path/to/img", 11.99, 0)
  session.add(dummy_product)
  session.commit()
  session.close()

  # reload products
  products = session.query(Product).all()

session.close()

# show existing users
print('### Users:')
for user in users:
  print(f'({user.id}) {user.first_name} {user.last_name} - {user.username}')

# new line
print()

# show existing users
print('### Products:')
for product in products:
  print(f'({product.id}) {product.name} - {product.description} - {product.price} - {product.image_url}')
