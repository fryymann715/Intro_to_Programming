import os
import notedb
import noteclasses

number_of_lessons = len(os.listdir(os.path.join(os.path.dirname(__file__), 'lesson_notes')))

# Library full of functions used to pull bits of data from the lesson notes text files.


# Function that finds the number of concepts in the lesson string by counting the amount of TITLE tasgs it finds
def get_num_of_concepts(text):
    number_concepts = 0
    while text.find('TITLE:') != -1:
        number_concepts += 1
        next_spot = text.find('TITLE:')
        text = text[next_spot+6:]
    return number_concepts


# pulls the lesson number from the lesson string returns it
def get_lesson_id(text):
    start_location = text.find('LESSON: ')
    end_location = text.find('NAME: ')
    lesson_id = text[start_location+8:end_location]
    lesson_id = lesson_id.rstrip()
    lesson_id = lesson_id.lstrip()
    return lesson_id


# pulls the lesson name from the lesson string
def get_lesson_name(text):
    start_location = text.find('NAME: ') + 6
    end_location = text.find('TITLE: ')
    lesson_name = text[start_location:end_location-1]
    lesson_name = lesson_name.lstrip()
    lesson_name = lesson_name.rstrip()
    return lesson_name


# pulls an individual concept from a chunk of the lesson string
def get_title(concept):
    start_location = concept.find('TITLE: ') + 7
    end_location = concept.find('DESC: ')
    concept_title = concept[start_location:end_location-1]
    return concept_title


# grabs the description portion of the raw concept text
def get_desc(concept):
    start_location = concept.find('DESC: ') + 6
    end_location = concept.find('TITLE: ', start_location)
    concept_desc = concept[start_location:end_location]
    return concept_desc


# loops through all the concepts and fills a list containing all the concepts' info
def fill_concepts(text, number_of_concepts):
    counter = 0
    concept_list = []
    while counter < number_of_concepts:
        concept = {}
        this_concept_start = text.find('TITLE:')
        this_concept_end = text.find('TITLE:', this_concept_start + 1)
        raw_concept = text[this_concept_start:this_concept_end]
        concept['title'] = get_title(raw_concept)
        concept['description'] = get_desc(raw_concept)
        concept_list.append(concept)
        text = text[this_concept_end:]
        counter += 1
    return concept_list


# Opens the lesson file, reads it and assigns it to a string. Returns said string.
def get_lesson_text(lesson_number):
    file_name = 'lesson_notes/'+lesson_number+'.txt'
    lesson_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    lessonfile = open(lesson_path, 'r')
    if lessonfile:
        lesson_text = lessonfile.read()
        lessonfile.close()
        return lesson_text


# Function that create the new datastore entries for a lesson utilizing my old code that
# built a Lesson object from all the data in the lesson text file.
def build_lesson_table(lesson_number):
    lesson = noteclasses.Lesson(lesson_number)
    lesson_table = notedb.Lesson_Note(parent=notedb.lesson_dir(lesson_number))

    lesson_table.name = lesson.name
    concept_id = 1
    for concept in lesson.concepts:
        concept_table = notedb.Concept(parent=notedb.lesson_db(lesson_number))
        concept_table.title = concept['title']
        concept_table.description = concept['description']
        concept_table.id_number = concept_id
        concept_table.put()
        concept_id += 1
    lesson_table.concepts = notedb.lesson_db(lesson_number)
    lesson_table.put()


# Creates and returns a list of dictionaries that hold the number and name of each lesson
def get_lesson_list():
    lesson_list = []
    for lesson in range(0,number_of_lessons):
        lesson_num = lesson + 1
        lesson_text = get_lesson_text(str(lesson_num))
        lesson_name = get_lesson_name(lesson_text)
        lesson_dict = {'number': str(lesson_num), 'name': lesson_name}
        lesson_list.append(lesson_dict)
    return lesson_list



