__author__ = "ideans"

# Import my classes and my functions
import note_classes
import lessonlib

# Assign the text from txt file to a string.

lessonfile = open("C:\Users\Ian\Documents\Intro to Programming\Lesson_9_`Notes.txt")
LESSON_TEXT = lessonfile.read()
lessonfile.close()

# Function that runs the needed and puts the data into a list that is used to create the lesson object.


def process_lesson_text():
    concept_list_string = lessonlib.fill_concepts(LESSON_TEXT, lessonlib.get_num_of_concepts(LESSON_TEXT))
    lesson_list = [lessonlib.get_lesson_name(LESSON_TEXT), lessonlib.get_lesson_id(LESSON_TEXT),
                   concept_list_string]
    return lesson_list

# List created to abstractly plug into constructor for lesson.
lesson_list = process_lesson_text()

lesson10 = note_classes.Lesson(lesson_list[0], lesson_list[1], lesson_list[2])
print(lesson10.get_html())