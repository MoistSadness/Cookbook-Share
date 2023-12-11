from flask import Flask, request, jsonify, make_response
import psycopg2
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)


################################################################
# Database connection

def ConnectToDB():
  connection = psycopg2.connect(
    database = environ.get('DB_NAME'),
    host= environ.get('DB_HOST'),
    user = environ.get('DB_USERNAME'),
    password = environ.get('DB_PASSWORD'),
    port = environ.get('DB_PORT')
  )
  if connection: print("Connected to database!", flush=True)
  return connection

def DisconnectFromDB(cursor): cursor.close()


################################################################
# Authentication
'''
User data should look like the following:
  id: string
  username: string
  pasword: string
  ssn: string
  recipies: recipie[]
'''


UsersRootURL = '/api/v1/users'
RecipiesRootURL = '/api/v1/recipies'

##################################################################
# @desc     Get all users
# route     GET     /api/v1/users
# @access   Public
@app.route(UsersRootURL, methods=['GET'])
def GetAllUsers():
  try:
    connection = ConnectToDB()
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    return make_response(jsonify(users), 200)
  except Exception as e:
    return make_response(jsonify({'message': str(e)}), 400)


##################################################################
# @desc     Register new user
# route     POST    /api/v1/users
# @access   Public
@app.route(UsersRootURL, methods=['POST'])
def RegisterNewUser():
  data = request.form.to_dict()
  #print(data, flush=True)
  salt = bcrypt.gensalt()
  hashed = bcrypt.hashpw(data["password"].encode('utf8'), salt)
  sql = """INSERT INTO Users (username, password, ssn) VALUES(%s, %s, %s) RETURNING username"""
  
  # Add user details to the database
  try:
    connection = ConnectToDB()
    cursor = connection.cursor()
    
    print("Executing query", flush=True)
    cursor.execute(sql, (data["username"], hashed, data["ssn"]) )
    
    inserted = cursor.fetchone()[0]
    
    print("Committing to DB", flush=True)
    connection.commit()
    cursor.close()
    return make_response(jsonify({'message': f"Registered {inserted}"}), 200)
  except Exception as e:
    return make_response(jsonify({'message': str(e)}), 400)


##################################################################
# @desc     Get one user
# route     GET    /api/v1/users/<username>
# @access   Public
@app.route(UsersRootURL + "/<username>", methods = ['GET'])
def GetOneUser(username):
  return make_response(jsonify({'message': f"Viewing {username}\'s Profile"}), 200)


##################################################################
# @desc     Update a user
# route     PUT    /api/v1/users/<username>
# @access   Private
@app.route(UsersRootURL + "/<username>", methods = ['PUT'])
def UpdateOneUser(username):
  return make_response(jsonify({'message': f"Updating {username}\'s Profile"}), 200)


##################################################################
# @desc     Delete a user
# route     DELETE    /api/v1/users/<username>
# @access   Private
@app.route(UsersRootURL + "/<username>", methods = ['DELETE'])
def DeleteOneUser(username):
  return make_response(jsonify({'message': f"Deleting {username}\'s Profile"}), 200)


##################################################################
# @desc     Get an authentication token
# route     POST    /api/v1/users/auth
# @access   Public
@app.route(UsersRootURL + "/<username>", methods = ['DELETE'])
def Authenticate(username):
  return make_response(jsonify({'message': f"Authenticating"}), 200)

# Log out






################################################################
################################################################
################################################################
# Recpipe Stuff

# Get all recipies
@app.route(RecipiesRootURL, methods=['GET'])
def GetAllRecipies():
  return make_response(jsonify({'message': 'All Recipies'}), 200)
  

# Get one recipie


# Create a recipie
@app.route(RecipiesRootURL, methods=['POST'])
def CreateRecipies():
  data = request.get_json()
  return make_response(jsonify({'message': 'Recipie Created'}), 200)

# Delete a recipie

#Error Handling
@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({
      "code": 404,
      "message": "Page not found"
    }
))