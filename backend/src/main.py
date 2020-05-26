# coding=utf-8

from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.user import User, UserSchema

# creating the flask application
app = Flask(__name__)

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
def add_exam():
  # mount the user object
  posted_user = UserSchema(only=('first_name', 'last_name', 'username')).load(request.get_json())
  user = User(**posted_user, creator=1)

  # persist the user
  session = Session()
  session.add(user)
  session.commit()

  # return the created user
  new_user = UserSchema().dump(user)
  session.close()
  return jsonify(new_user), 201

# start session
session = Session();

# check for existing data
users = session.query(User).all()

if len(users) == 0:
  # create and persist dummy user
  dummy_user = User("Caleb", "Penn", "cpenn", 0)
  session.add(dummy_user)
  session.commit()
  session.close()

  # reload users
  users = session.query(User).all()

# show existing users
print('### Users:')
for user in users:
  print(f'({user.id}) {user.first_name} {user.last_name} - {user.username}')
