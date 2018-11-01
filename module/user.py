# from app import db
from database.mysql_db import db
# print(db)
class User(db.Model):
	__tablename__ = 'my_user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)

	def __init__(self, username, email):
		self.username = username
		self.email = email
	def __repr__(self):
		return '<User %r>' % self.username        

# db.create_all()
# db.drop_all()