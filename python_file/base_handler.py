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
from google.appengine.ext.webapp import template
from google.appengine.ext import db
import os
from jinja2 import Environment, FileSystemLoader
import re
import hashlib
import random,string
import logging

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env= Environment(loader=FileSystemLoader(template_dir),
                                autoescape=True)
class BaseHandler(webapp2.RequestHandler):
   
    def write(self, *a, **kw):
    	self.response.out.write(*a,**kw)
    def render_str(self,template,**params):
        t=jinja_env.get_template(template)
        return t.render(params)
    def render(self, template,**kw):
        self.write(self.render_str(template,**kw))
#########################################################################################3
    def salt():
        return "".join(random.choice(string.letters)for x in xrange(5))
    hash_salt="bill"
    def hash_str(self,value):
        return hashlib.md5(value).hexdigest()
    def make_secure_val(self,value):
        return "%s|%s" %(value,self.hash_str(str(value)+str(self.hash_salt)))

    def check_secure_val(self,value):
        val=value.split('|')[0]
        if value==self.make_secure_val(val):
            return val
    def set_cookie(self,cookie_name,cookie_val):
    	hash_val=self.make_secure_val(cookie_val)
    	self.response.headers.add_header('Set-Cookie','%s=%s' % (cookie_name,hash_val))

class Sign_BaseHandler(BaseHandler):
	def check_already_login(self):
		cookie=self.request.cookies.get('user_key')
		if cookie:
			return True
		
