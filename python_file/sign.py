#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.ext import db
import base_handler
from base_handler import BaseHandler
from base_handler import Sign_BaseHandler

class User_data(db.Model):
	name=db.StringProperty(required=True)
	password=db.StringProperty(required=True)
	email=db.StringProperty(required=True)
	@classmethod
	def by_name(cls, username):
		user = User_data.all().filter('name =', username).get()
		return user

	@classmethod
	def login(cls,name,pw):
		u=cls.by_name(name)
		if u :
			if u.password==pw:
				return u.key()
			else:
				return "pw_error"
		else:
			return "name_error"

class Signup(Sign_BaseHandler):
	def get(self):
		self.redirect('/')
	
	def post(self):
		name_error="The format of your name is wrong."
		pw_error="The format of your password is wrong."
		v_error="Didn't varify"
		email_error="This isn't a email."
		exist_error=""

		name=str(self.request.get("name"))
		pw=str(self.request.get("password"))
		vpw=str(self.request.get("v_password"))
		email=str(self.request.get("email"))

		user_exist= User_data.by_name(name)
		#self.request.get("home")
		if len(name)>=3 and len(name)<=10:
			name_error=""
		if len(pw)>=3 and len(pw)<=20:
			pw_error=""
		if pw==vpw:
			v_error=""
		if "@"in email:
			email_error=""
		
		if user_exist:
			exist_error="This user is already exist"



		if name_error=="" and email_error=="" and v_error=="" and pw_error=="" and exist_error=="":
			user_data_put=User_data(name=name,password=pw,email=email)
			user_data_put.put()
			user_key=user_data_put.key()
			self.set_cookie("user_key",user_key)
			
			self.redirect('/')

		else:
			self.render("signup_login.html",
			name_error=name_error,
			pw_error=pw_error,
			v_error=v_error,
			email_error=email_error,
			exist_error=exist_error
			)

class Login(Sign_BaseHandler):
	def get(self):
		self.redirect('/')
# need to be change here
	def post(self):
		name=str(self.request.get("login_name"))
		pw=str(self.request.get("login_pw"))

		name_n_exist=""
		pw_error=""

		check_mark=User_data.login(name,pw)
		if check_mark=="name_error":
			name_n_exist="Your name doesn't exist"
			self.render("signup_login.html",login_name_error=name_n_exist)
		elif check_mark=="pw_error":
			pw_error="Forget your password !?"
			self.render("signup_login.html",login_pw_error=pw_error)
		else:
			self.set_cookie("user_key",check_mark)
			self.redirect('/')

class Logout(Sign_BaseHandler):
	def get(self):
		self.response.headers['Content-Type']='text/plain'
		self.response.headers.add_header('Set-Cookie','user_key=;')
		self.redirect('/')




		





