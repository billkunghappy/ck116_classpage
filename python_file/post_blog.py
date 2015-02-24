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

class Post(db.Model):
    title=db.StringProperty(required=True)
    word=db.TextProperty(required=True)
    created=db.DateTimeProperty(auto_now_add=True)
    name=db.StringProperty(required=True)

class Blog_page(Sign_BaseHandler):
    def get(self):
		posts=db.GqlQuery('select * from Post order by created desc limit 10')


		error_msg=""
		dropdown="Log in"
		login_error_msg=""
		cookie=self.request.cookies.get('user_key')
		check=None
		if cookie:
			check=self.check_secure_val(cookie)
		if check:
			user=db.get(check)
			username=str(user.name)
			error_msg="Log out first if you want to sign up"
			login_error_msg="Log out first if you want to log in"
			dropdown="Log out"
			self.set_cookie("user",username)
			self.render("blog.html",dropdown=dropdown,flag="yes",error_msg=error_msg,
			login_error_msg=login_error_msg,posts=posts)
		else:
			self.render("blog.html",dropdown=dropdown,flag="false",error_msg=error_msg,
								login_error_msg=login_error_msg,posts=posts)
	
    def post(self):
    	posts=db.GqlQuery('select * from Post order by created desc limit 10')
        title=self.request.get("title")
        word=self.request.get("word")
        name=self.request.cookies.get('user')
        username=None
        if name:
        	username=self.check_secure_val(name)
        
        terror=""
        werror=""

        if username:
            if title!="" and word!="":
                w=Post(title=title,word=word,name=username)
                w.put()
                self.redirect('/blog')
            else:
                if title=="":
                    terror="You didn't enter the title!"
                if word=="":
                    aerror="You didn't enter anything!"
                self.render('blog.html',title=title,word=word,
                	terror=terror,werror=werror,posts=posts,dropdown="Log out")
        else:
            self.render('blog.html',title=title,word=word,
                	terror=terror,werror=werror,posts=posts,dropdown="Log out")
# class Blog_new(BaseHandler):
#     def get(self):
#         key.db.from_path('post',int(post_id),parent=blog_key)
#         post=db.get(key)
#         if not post:
#             self.error(404)
#             return
#         self.render("blog_new",post=post)





















	# userkey=None
		# if cookie:
		# 	userkey=self.check_secure_val(cookie)
		# 	if userkey:
		# 		user=db.get(userkey)
		# 		if user:
		# 			username=str(user.name)
		# 			self.set_cookie("user",username)
		# 			self.render("blog.html",dropdown=dropdown,flag="yes",error_msg=error_msg,
		# 						login_error_msg=login_error_msg)
		# 		else:
		# 			self.render("blog.html",dropdown=dropdown,flag="false",error_msg=error_msg,
		# 						login_error_msg=login_error_msg)
		# 	else:
		# 		self.render("blog.html",dropdown=dropdown,flag="false",error_msg=error_msg,
		# 						login_error_msg=login_error_msg)
		# else:
		# 	self.render("blog.html",dropdown=dropdown,flag="false",error_msg=error_msg,
		# 						login_error_msg=login_error_msg)