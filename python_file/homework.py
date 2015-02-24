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

class Homework(db.Model):
    work=db.StringProperty(required=True)
    subject=db.StringProperty(required=True)
    year=db.IntegerProperty(required=True)
    month=db.IntegerProperty(required=True)
    day=db.IntegerProperty(required=True)

# class Create_work(Sign_BaseHandler):
#     def get(self):
#         self.redirect('/')
#     def post(self):
#         cookie=self.request.cookies.get('user_key')
#         check=None
#         if cookie:
#             check=self.check_secure_val(cookie)
#         if check:
#             work=self.request.get('work')
#             subject=self.request.get('subject')
#             year=self.request.get('year')
#             month=self.request.get('month')
#             day=self.request.get('day')
            

class Work_page(Sign_BaseHandler):
    def get(self):
        error_msg=""
        dropdown="Log in"
        login_error_msg=""
        cookie=self.request.cookies.get('user_key')
        check=None
        if cookie:
            check=self.check_secure_val(cookie)
        else:
            self.redirect('/')
        if check:
            error_msg="Log out first if you want to sign up"
            login_error_msg="Log out first if you want to log in"
            dropdown="Log out"
            self.render("work.html",error_msg=error_msg,
            login_error_msg=login_error_msg,dropdown=dropdown)
        else:
            self.redirect('/')
    # def post(self):
		