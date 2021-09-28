import datetime

class TrainingCentre:
    # A static private variable that increments each time the constructor is called
    __counter = 0

    def __init__(self, name, opening_date = datetime.date.today()):
        TrainingCentre.__counter += 1
        self.__id = TrainingCentre.__counter
        self.__name = name
        self.__date_opened = opening_date
        self.__capacity = 100

    @property
    def ID(self):
        return self.__id

    @property
    def Name(self):
        return self.__name

    @property
    def DateOpened(self):
        return self.__date_opened

    @property
    def Capacity(self):
        return self.__capacity