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

import base_handler
from base_handler import BaseHandler
from base_handler import Sign_BaseHandler

class User_data(db.Model):
	name=db.StringProperty(required=True)
	password=db.StringProperty(required=True)
	email=db.StringProperty(required=True)
#pull fb API
	@classmethod
    def by_name(cls, username):
        u = User_data.all().filter('name =', username).get()
        return u



	#hotel_rank
	#compare hotel_score(not in database)

class Hotel_value(db.Model):
	user=db.StringProperty(required=True)
	hotel_score=db.FloatProperty(required=True)
	hotel_evaluate=db.StringProperty(required=True)
