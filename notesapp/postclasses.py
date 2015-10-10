__author__ = 'Ian'

from google.appengine.ext import ndb

DEFAULT_WALL = "None"


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