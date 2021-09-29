import random
from TrainingCentre import TrainingCentre
import GUI


class Simulation:
    def __init__(self, default_welcome=True):
        length, centre_count = GUI.welcome_func(default_welcome)
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
            self.__training_centres.append(self.__open_new_centre())

        self.__simulation_output = {
            "Open Centres": 0,
            "Full Centres": 0,
            "Trainees Training": 0,
            "Trainees Waiting": 0
        }

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
    def SimulationResults(self):
        return self.__simulation_output.copy()

    @property
    def Training_Centres(self):
        return self.__training_centres

    def __open_new_centre(self):
        # self.__training_centres.append(TrainingCentre())
        return TrainingCentre()

    def __recruit_trainees(self):
        new_trainees = random.randint(20, 30)
        # Append these trainees to waiting list
        self.__trainees["Waiting"] += new_trainees
        return new_trainees  # The number of trainees to generate (not needed but nice)

    def run_simulation(self):
        # MAIN LOOP - Go through the simulation month by month
        month_list = {}
        for month in range(1, self.__simulation_length + 1):
            # Every month, new trainees are recruited/generated
            self.__recruit_trainees()


            # On an even month, a new centre opens
            if month % 2 == 0:
                self.__training_centres.append(self.__open_new_centre())

            # Debug (Remove)
            print(f"\nMonth {month}")
            print(f"Total Training Centres: {len(self.__training_centres)}")
            print(f"Trainees currently in training: {self.__trainees['Training']}")
            print(f"Trainees currently in waiting : {self.__trainees['Waiting']}")
            print(f"Now attempting to place trainees\n{'-' * 50}")

            open_centres_count = full_centres_count = 0
            # Sift through waiting list and add trainees to centres
            for centre in self.__training_centres:
                if not centre.IsFull:
                    open_centres_count += 1
                else:
                    full_centres_count += 1
                    continue  # This centre is full so dont bother adding from the waiting list

                # Add as many trainees to this centre
                placed = centre.add_trainees(self.__trainees["Waiting"])
                self.__trainees["Waiting"] -= placed
                self.__trainees["Training"] += placed

            # Debug (remove)
            print(f"Trainees now in training: {self.__trainees['Training']}")
            print(f"Trainees now in waiting : {self.__trainees['Waiting']}")

            month_list[month] = {
                "TraineesTraining": self.__trainees['Training'],
                "TraineesWaiting": self.__trainees['Waiting'],
                "OpenCentres": 0,
                "FullCentres": 0
            }

        # End of simulation report
        self.__simulation_output["Full Centres"] = sum([centre.IsFull for centre in self.__training_centres])
        self.__simulation_output["Open Centres"] = len(self.__training_centres) - self.__simulation_output[
            "Full Centres"]
        self.__simulation_output["Trainees Training"] = self.__trainees['Training']
        self.__simulation_output["Trainees Waiting"] = self.__trainees['Waiting']

        full_centre_list = []
        open_centre_list = []

        for centre in self.__training_centres:
            if centre.IsFull:
                self.__simulation_output["Full Centres"].append(centre)
            else:
                self.__simulation_output["Open Centres"].append(centre)

        GUI.print_simulation_results(self.SimulationResults)
        # GUI.display_graph(month_list, full_centre_list)

    # Testing Getters:
    def get_open_new_centres(self):
        self.__open_new_centre()

    def get_recruit_trainees(self):
        return self.__recruit_trainees()


# Test
sim = Simulation()
sim.run_simulation()
