__author__ = "ideans"

import lessonlib
import notedb
import postclasses

from google.appengine.api import users


# The Lesson class builds a lesson object that holds the data for each lesson based
# on the note file in the lesson_notes directory.
class Lesson:

    def __init__(self, lesson_number):

        lesson_text = lessonlib.get_lesson_text(lesson_number)
        self.name = lessonlib.get_lesson_name(lesson_text)
        self.concepts = lessonlib.fill_concepts(lesson_text, lessonlib.get_num_of_concepts(lesson_text))


# This is the class that holds all the 'goods' in one object to make
# rendering templates less messy.
class Dgoods:

    def __init__(self, lesson_number=None, error_code=0):
        self.lesson_list = lessonlib.get_lesson_list()
        if lesson_number:
            lesson_query = notedb.Lesson_Note.query(ancestor=notedb.lesson_dir(lesson_number))
            concept_query = notedb.Concept.query(ancestor=notedb.lesson_db(lesson_number)).order(+notedb.Concept.id_number)
            lesson = lesson_query.fetch()
            concepts = concept_query.fetch()

            self.lesson_name = lesson[0].name
            self.lesson_number = lesson_number
            self.concept_list = concepts

        user = users.get_current_user()
        if user:
            if lesson_number:
                post_query = postclasses.Post.query(ancestor = postclasses.lesson_key(lesson_number))\
                .filter(postclasses.Post.author.identity == user.user_id()).order(-postclasses.Post.date)
                self.posts = post_query.fetch()

            self.user_name = user.nickname()
            self.user_url = users.create_logout_url('/')
            self.user_linktext = "Logout"
            self.is_user = True
        else:
            self.user_name = "Not Logged In"
            self.user_url = users.create_login_url('/')
            self.user_linktext = "Login"
            self.is_user = False
            self.posts = None

        if error_code == 1:
            self.error_message = "Sorry but that is not a valid lesson number. Please select from the menu."
        elif error_code == 2:
            self.error_message = "Note must have content, please resubmit with something worth noting!"


