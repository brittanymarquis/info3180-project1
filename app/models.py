from flask import json, jsonify
from . import db

class UserProfile(db.Model):
	  __tablename__ = "users"
	  id = db.Column(db.Integer, primary_key=True)
	  firstname 		= db.Column(db.String(80))
	  lastname 		    = db.Column(db.String(80))
	  gender			= db.Column(db.String(10))
	  email             = db.Column(db.String(80))
	  location          = db.Column(db.String(80))
	  bio 			    = db.Column(db.String(250))
	 
	 
	  
	  def __init__(self,firstname,lastname,gender,email,location,bio,):
		self.firstname   	= firstname
		self.lastname 		= lastname
		self.gender 		= gender
		self.email 	    	= email
		self.location 		= location
		self.bio 			= bio
		
		
		
		def __repr__(self):
			return "User: {0} {1}".format(self.firstname, self.lastname)