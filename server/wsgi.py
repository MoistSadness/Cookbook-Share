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

# Get all users
@app.route('/api/v1/recipies', methods=['GET'])
def GetAllUsers():
  connection = ConnectToDB()
  cursor=connection.cursor()
  cursor.execute('SELECT * FROM Users')
  users = cursor.fetchall()
  
  return make_response(jsonify(users), 200)

# Register new user
@app.route('/api/v1/recipies', methods=['POST'])
def RegisterNewUser():
  data = request.get_json()
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
    return make_response(jsonify({'message': str(e)}), 200)

# Delete user

# Log in

# Get Access Token

# Get Refresh Token


################################################################
# Recpipe Stuff

# Get all recipies
@app.route('/api/v1/recipies', methods=['GET'])
def GetAllRecipies():
  return make_response(jsonify({'message': 'All Recipies'}), 200)
  

# Get one recipie


# Create a recipie
@app.route('/api/v1/recipies', methods=['POST'])
def CreateRecipies():
  data = request.get_json()
  return make_response(jsonify({'message': 'Recipie Created'}), 200)

# Delete a recipie

















################################################################
# This is the original sample code
'''
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {'id': self.id,'username': self.username, 'email': self.email}

# App context needs to be active if the database is to be used
with app.app_context():
  db.create_all()

#create a test route
@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'My test!'}), 200)


# create a user
@app.route('/users', methods=['POST'])
def create_user():
  try:
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({'message': 'user created'}), 201)
  except Exception as e:
    print(e)
    return make_response(jsonify({'message': 'error creating user'}), 500)

# get all users
@app.route('/users', methods=['GET'])
def get_users():
  try:
    users = User.query.all()
    return make_response(jsonify([user.json() for user in users]), 200)
  except:
    return make_response(jsonify({'message': 'error getting users'}), 500)

# get a user by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      return make_response(jsonify({'user': user.json()}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except:
    return make_response(jsonify({'message': 'error getting user'}), 500)

# update a user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      data = request.get_json()
      user.username = data['username']
      user.email = data['email']
      db.session.commit()
      return make_response(jsonify({'message': 'user updated'}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except:
    return make_response(jsonify({'message': 'error updating user'}), 500)

# delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      db.session.delete(user)
      db.session.commit()
      return make_response(jsonify({'message': 'user deleted'}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except:
    return make_response(jsonify({'message': 'error deleting user'}), 500)
    '''