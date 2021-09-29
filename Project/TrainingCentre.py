import datetime


class TrainingCentre:
    # A static private variable that increments each time the constructor is called
    __counter = 0

    def __init__(self, name=None, opening_date = datetime.date.today()):
        type(self).__counter += 1
        self.__id = type(self).__counter

        self.__name = name
        if name is None:
            self.__name = f"Centre {self.__id}"

        self.__date_opened = opening_date
        self.__capacity = 0

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

    @property
    def IsFull(self):
        return self.__capacity >= 100

    # This function attempts to add trainees to this centre
    # It returns the amount of trainees succesfully added
    def add_trainees(self, count: int = 0):
        self.__capacity += count

        # Check if centre is over capacity:
        if self.__capacity > 100:
            trainees_added = count - (self.__capacity - 100)
            self.__capacity = 100
            return trainees_added

        return count

# Test
tc1 = TrainingCentre("1")
tc1.add_trainees(90)
print(tc1.IsFull)
tc1.add_trainees(1)
print(tc1.IsFull)