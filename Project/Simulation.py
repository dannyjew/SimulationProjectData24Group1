import random
from TrainingCentre import TrainingCentre
from UI import *

class Simulation:
    def __init__(self):
        length, centre_count = welcome_func()
        self.__simulation_length = length

        # A dictionary containing ALL trainees split by those in training and waiting
        self.__trainees = {
            "Training": 0,
            "Waiting": 0
        }

        # A dictionary of ALL training centres split into three categories
        self.__training_centres = []

        # Initially create as many training centres as requested by user
        for i in range(centre_count):
            self.__open_new_centre()


        self.__open_count = self.__full_count = 0

    @property
    def OpenCount(self):
        return self.__open_count

    @property
    def FullCount(self):
        return self.__full_count

    @property
    def SimulationLength(self):
        return self.__simulation_length

    @property
    def Waiting_List(self):
        return self.__trainees["Waiting"]

    @property
    def Training_Centres(self):
        return self.__training_centres

    def __open_new_centre(self):
        self.__training_centres.append(TrainingCentre())

    def __recruit_trainees(self):
        new_trainees = random.randint(20, 30)
        # Append these trainees to waiting list
        self.__trainees["Waiting"] += new_trainees
        return new_trainees  # The number of trainees to generate (not needed but nice)

    # TODO: Consider implementing a UI class



    def run_simulation(self):
        # MAIN LOOP - Go through the simulation month by month
        for month in range(1, self.__simulation_length + 1):
            # Every month, new trainees are recruited/generated
            self.__recruit_trainees()

            # On an even month, a new centre opens
            if month % 2 == 0:
                self.__open_new_centre()

            # Debug (Remove)
            print(f"\nMonth {month}")
            print(f"Total Training Centres: {len(self.__training_centres)}")
            print(f"Trainees currently in training: {self.__trainees['Training']}")
            print(f"Trainees currently in waiting : {self.__trainees['Waiting']}")
            print(f"Now attempting to place trainees\n{'-' * 50}")

            # Sift through waiting list and add trainees to centres
            for centre in self.__training_centres:
                # All trainees placed so you can stop loop
                if self.__trainees["Waiting"] == 0:
                    break

                # Add as many trainees to this centre
                placed = centre.add_trainees(self.__trainees["Waiting"])
                self.__trainees["Waiting"] -= placed
                self.__trainees["Training"] += placed

            # Debug (remove)
            print(f"Trainees now in training: {self.__trainees['Training']}")
            print(f"Trainees now in waiting : {self.__trainees['Waiting']}")


        # End of simulation report
        self.__full_count = sum([centre.IsFull for centre in self.__training_centres])
        self.__open_count = len(self.__training_centres) - self.__full_count

        print(f"""\n\n{'-'*50}\nEnd of Simulation Report
        Number of open centres: {self.__open_count}
        Number of full centres: {self.__full_count}
        Number of trainees in training: {self.__trainees['Training']}
        Number of trainees in waiting : {self.__trainees['Waiting']}
End of End of Simulation Report\n{'-'*50}""")

        # Testing Getters:
        def get_open_new_centres(self):
            self.__open_new_centre()

        def get_recruit_trainees(self):
            return self.__recruit_trainees()

        def get_welcome_func(self):
            return self.__welcome_func()



# Test
sim = Simulation()
sim.run_simulation()
