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
import jinja2

import cgi
import urllib
import os

from google.appengine.api import users
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

DEFAULT_WALL = 'Home'

def lesson_key(lesson_number=DEFAULT_WALL):
    return ndb.Key('Lesson', lesson_number)


class Author(ndb.Model):
    identity = ndb.StringProperty(indexed=True)
    name = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=True)


class Post(ndb.Model):
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


# class Concept(ndb.Model):
#     title = ndb.StringProperty(indexed=False)
#     description = ndb.StringProperty(indexed=False)
#
#
# class Lesson(ndb.Model):
#     # id_number = ndb.Key(indexed=True)
#     name = ndb.StringProperty(indexed=False)
#     concept = ndb.StructuredProperty(Concept)



class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainHandler(Handler):
    def get(self):

        lesson_number = self.request.get("lesson_number", DEFAULT_WALL)
        user = users.get_current_user()
        if lesson_number:
            if lesson_number == DEFAULT_WALL.lower(): lesson_number=DEFAULT_WALL
            user_dict = {}
            if user:
                user_dict = {'url': users.create_logout_url(self.request.uri),
                             'url_linktext': "Logout",
                             'user_name': user.nickname(),
                             'is_user': True}
                post_query = Post.query(ancestor = lesson_key(lesson_number))\
                    .filter(Post.author.identity == user.user_id()).order(-Post.date)
            else:
                user_dict = {'url': users.create_login_url(self.request.uri),
                             'url_linktext': "Login",
                             'user_name': 'Not Logged In'}
                post_query = Post.query(ancestor = lesson_key(lesson_number))\
                    .filter(Post.author.name == 'Anonymous').order(-Post.date)


            posts = post_query.fetch()

            if posts:
                # users_posts = []
                # for post in posts:
                #     if user.user_id() == post.author.identity: users_posts.append(post)

                self.render("with_content.html", user=user_dict, lesson_number=lesson_number, posts=posts)
            else:
                self.render("base.html", user=user_dict, lesson_number=lesson_number)
        # else:
        #     self.render("base.html")


class SignHandler(Handler):
    def post(self):
        content = self.request.get('content')
        lesson_number = self.request.get('lesson_number')

        post = Post(parent=lesson_key(lesson_number))

        if users.get_current_user():
            post.author = Author(
            identity=users.get_current_user().user_id(),
            name=users.get_current_user().nickname(),
            email=users.get_current_user().email()
            )
        else:
            post.author = Author(
                name="Anonymous",
                email="Anonymous"
                )
        post.content = content
        post.put()

        redirect_string = "/?lesson_number=%s" % lesson_number

        self.redirect(redirect_string)


class LessonSwitch(MainHandler):
    def get(self):
        lesson_number = self.request.get('lesson_number')
        # user = users.get_current_user()
        if lesson_number:
            self.redirect('/?lesson_number=%s' % lesson_number)
        else:
            self.redirect('/')





app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/sign', SignHandler),
    ('/switch_lesson', LessonSwitch)
], debug=True)
