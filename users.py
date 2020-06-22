"""
Object representation of Users, plus functions to store and retrieve Users from the database.

Behrad Koohy (@behradkoohy) 2020
"""
import logging
from database import myDb
from flask_login import LoginManager, UserMixin

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
	print(mongo.get_all("moderators")[0])
	return mongo.get_one("moderators", {"email": email})