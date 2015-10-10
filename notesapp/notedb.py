__author__ = 'Ian'

from google.appengine.ext import ndb
import lessonhandlers

LESSON_DIR = "0"
DEFAULT_LESSON = '0'


def lesson_dir(lesson_note=LESSON_DIR):
    return ndb.Key('Lesson_Number', lesson_note)


def lesson_db(lesson_number=DEFAULT_LESSON):
    return ndb.Key('Concepts_in_Lesson', lesson_number)


class Concept(ndb.Model):
    title = ndb.StringProperty(indexed=False)
    description = ndb.StringProperty(indexed=False)
    id_number= ndb.IntegerProperty(indexed=True)


class Lesson_Note(ndb.Model):
    name = ndb.StringProperty(indexed=True)
    concepts = ndb.KeyProperty(indexed=True)


