__author__ = 'Ian'

# Library full of functions used to pull bits of data from the lesson notes text files.


# function that finds the number of concepts in the lesson string by counting the amount of TITLE tasgs it finds


def get_num_of_concepts(text):
    number_concepts = 0
    while text.find('TITLE:') != -1:
        number_concepts += 1
        next_spot = text.find('TITLE:')
        text = text[next_spot+6:]
    return number_concepts

# pulls the lesson number from the lesson string and turns it into an integer


def get_lesson_id(text):
    start_location = text.find('LESSON: ')
    end_location = text.find('NAME: ')
    lesson_id = text[start_location+8:end_location]
    lesson_id = lesson_id.rstrip()
    lesson_id = lesson_id.lstrip()
    return lesson_id

# takes the number that is passed to it and increments it by 1


def gen_concept_id(id_number):
    id_number = int(id_number)
    id_number += 1
    return str(id_number)

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
        concept_id = gen_concept_id(counter)
        concept = [0] * 3
        this_concept_start = text.find('TITLE:')
        this_concept_end = text.find('TITLE:', this_concept_start + 1)
        raw_concept = text[this_concept_start:this_concept_end]
        concept[0] = concept_id
        concept[1] = get_title(raw_concept)
        concept[2] = get_desc(raw_concept)
        concept_list.append(concept)
        text = text[this_concept_end:]
        counter += 1
    return concept_list



