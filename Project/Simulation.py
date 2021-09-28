import random
from TrainingCentre import TrainingCentre


class Simulation:
    def __init__(self):
        length, centre_count = self.__welcome_func()
        self.__simulation_length = length

        # A dictionary containing ALL trainees split by those in training and waiting
        self.__trainees = {
            "Training": 0,
            "Waiting": 0
        }

        # A dictionary of ALL training centres split into three categories
        self.__training_centres = []

        # Initially create as many training centres as requested by user
        map(self.__open_new_centre(), range(centre_count))

    @property
    def SimulationLength(self):
        return self.__simulation_length

    @property
    def Waiting_List(self):
        return self.__trainees["Waiting"]

    def __open_new_centre(self):
        self.__training_centres.append(TrainingCentre())

    def __recruit_trainees(self):
        new_trainees = random.randint(20, 30)
        # Append these trainees to waiting list
        self.__trainees["Waiting"] += new_trainees
        return new_trainees  # The number of trainees to generate (not needed but nice)

    # TODO: Consider implementing a UI class
    @staticmethod
    def __welcome_func():
        # These are all user input captures
        user_input = ""
        length = "3"
        centre_count = "1"

        # 1. Initial Screen with Simulation Settings
        print(f"""Simulation Settings\n{'-' * 50}
            Default Settings:
                Simulation Length (month):              {length}
                Initial Amount of Training Centres:     {centre_count}\n""")
        print("1. Run simulation with defaults")
        print("2. Change simulation settings\n")

        while True:
            user_input = input("Select an option: ")
            if user_input.isnumeric() and int(user_input) in range(1, 3):
                # Return the default settings
                if user_input == "1":
                    return int(length), int(centre_count)
                break

        # 2. User wants to manually change settings
        while True:
            length = input("Enter Simulation Length (in months): ")
            if length.isnumeric() and int(length) > 0:
                break

        while True:
            centre_count = input("Enter the number of Training Centres at Simulation start: ")
            if centre_count.isnumeric() and int(centre_count) > 0:
                break

        return int(length), int(centre_count)

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
        full_count = sum([centre.IsFull for centre in self.__training_centres])
        open_count = len(self.__training_centres) - full_count

        print(f"""\n\n{'-'*50}\nEnd of Simulation Report
        Number of open centres: {open_count}
        Number of full centres: {full_count}
        Number of trainees in training: {self.__trainees['Training']}
        Number of trainees in waiting : {self.__trainees['Waiting']}
End of End of Simulation Report\n{'-'*50}""")



# Test
sim = Simulation()
sim.run_simulation()