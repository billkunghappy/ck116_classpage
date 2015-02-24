#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
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
import sys
sys.path.append("python_file")
###############################################################################
import base_handler
from base_handler import BaseHandler
from base_handler import Sign_BaseHandler
###############################################################################
###############################################################################
import sign
from sign import User_data
from sign import Signup
from sign import Login
from sign import Logout

###############################################################################
import post_blog
from post_blog import Post
from post_blog import Blog_page
###############################################################################
import homework
from homework import Work_page







class MainHandler(Sign_BaseHandler):
	def get(self):
		error_msg=""
		dropdown="Log in"
		login_error_msg=""
		check=self.check_already_login()
		if check:
			error_msg="Log out first if you want to sign up"
			login_error_msg="Log out first if you want to log in"
			dropdown="Log out"

		self.render("class_about_page.html",error_msg=error_msg,
			login_error_msg=login_error_msg,dropdown=dropdown)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signupenter', Signup),
    ('/loginenter', Login),
    ('/logout', Logout),
    ('/blog', Blog_page),
    ('/work', Work_page)

], debug=True)
