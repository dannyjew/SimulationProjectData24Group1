class Trainees():

    def __init__(self, id, centre, name="A", course_length=3):
        self.__id = id
        self.__name = name
        self.__training_centre = centre
        self.__course_length = course_length

    @property
    def ID(self):
        return self.__id

    @property
    def Name(self):
        return self.__name

    @property
    def Centre(self):
        return self.__training_centre

    @property
    def Course_length(self):
        return self.__course_length

    def add_to_training_centre(self, centre):
        return True

