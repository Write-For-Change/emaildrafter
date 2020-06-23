"""
Object representation of Users, plus functions to store and retrieve Users from the database.

Behrad Koohy (@behradkoohy) 2020
"""
import logging
from database import myDb
from flask_login import LoginManager, UserMixin
from flask.json import JSONEncoder
from bson import json_util
from bson.objectid import ObjectId

class CustomJSONEncoder(JSONEncoder):
	def default(self, obj): return json_util.default(obj)


class User(UserMixin):

	def __init__(self, id, name, email, password, state):
		self.id = id
		self.name = name
		self.email = email
		self.password = password
		self.state = state

	def is_authenticated(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id

	def __repr__(self):
		return self.name

# Instantiate the db connection:
mongo = myDb()

def add_user(**t):
	ts = locals()['t']
	ts['state'] = 'user'
	mongo.insert_one("moderators", ts)
	return True

def find_user(email):
	return mongo.get_one("moderators", {"email": email})


def user_loader_db(oid):
	# print(oid, type(oid), "USER LOADER USER.PY", ObjectId(oid), type(ObjectId(oid)))
	return mongo.get_one("moderators", {"_id": ObjectId(oid['$oid'])})

