from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Users(Resource):
  def get(self);
    return {'users': [{'id':1, 'name':'Caleb'},{'id':2, 'name':'David'}]}

api.add_resource(Users, '/users') # Route_1

if __name__ == '__main__':
  app.run(port=5002)
