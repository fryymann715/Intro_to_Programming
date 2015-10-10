__author__ = "ideans"

class Entry():

    def __init__(self, title, id_number):
        self.title = title
        self.id_number = id_number

    def get_title(self):
        return self.title

    def get_id_number(self):
        return self.id_number


class Concept(Entry):

    def __init__(self, title, id_number, lesson_id, desc):
        Entry.__init__(self, title, id_number)
        self.lesson_id = lesson_id
        self.desc = desc
        self.html_string = '''
            <div class="concept">
                <span class="concept-title" id="lesson''' + self.lesson_id + '-' + self.title + '">' + self.id_number + '''</span>
                    <p>
                        ''' + self.desc + '''
                    </p>
            </div>'''

    def get_desc(self):
        return self.desc

    def get_html(self):
        return self.html_string


class Lesson(Entry):

    def __init__(self, title, id_number, concept_list_string):
        Entry.__init__(self, title, id_number)
        self.concept_list_string = concept_list_string
        self.concept_list = []
        self.build_concepts()


    def build_concepts(self):
        for item in self.concept_list_string:
            title = item[0]
            concept_id = item[1]
            desc = item[2]
            concept = Concept(title, concept_id, self.id_number, desc)
            self.concept_list.append(concept)

    def generate_concepts_html(self, concept_list):
        html_string = ''
        for item in concept_list:
            html_string = html_string + item.get_html()
        return html_string

    def get_html(self):
        return """
    <div class="lesson">
        <h1 id="lesson-""" + str(self.id_number) + '">' + self.title + '''</h1>''' + self.generate_concepts_html(self.concept_list) + '''
    </div>'''


    def get_concept(self, concept_number):
        return self.concept_list[concept_number]




