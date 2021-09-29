import random


class Simulation:
    def __init__(self, state: str, available_states: tuple, length: bool):
        self.__state = state
        self.__available_states = available_states
        self.__length = length
        self.current_month = 0
        self.total_centres = 0
        self.full_centres = 0
        self.trainees = []
        self.__waiting_list = []
        self.welcome_func()
        self.open_centres = self.total_centres - self.full_centres

    @property
    def State(self):
        return self.__state

    @property
    def Available_States(self):
        return self.__available_states

    @property
    def Length(self):
        return self.__length

    @property
    def Waiting_List(self):
        return self.__waiting_list

    def welcome_func(self):
        print("\n --- Welcome to the Sparta Simulation ---\n")

    def add_new_centre(self):
        self.total_centres += 1
        centre_list.append(training_centre())

    def add_from_waiting_list(self, waiting_list, centre_list, num):
        waiting_list.members = 0
        for centre in centre_list:
            num = centre.add_trainees(num)
        waiting_list.add(num)

    def assign_trainees(self, waiting_list, centre_list, num):
        total = 0
        for centre in centre_list:
            num = centre.add_trainees(num)
            if centre.is_full:
                total += 1
            waiting_list.add(num)
            self.full_centres = total

    def total_trainees(self, centres):
        total = 0
        for centre in centres:
            total += centre.members
        return total

    def generate_trainees(self):
        num = random.randint(20, 30)
        print(f"rand number = {num}")
        return num
