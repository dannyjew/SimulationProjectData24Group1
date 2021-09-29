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


        self.__simulation_output = {0: {
            "Training": 0,
            "Waiting": 0,
            "Full": 0,
            "Open": centre_count
        }}
        self.__final_simulation_output = self.__simulation_output[0]



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

        return self.__final_simulation_output.copy()


    @property
    def Training_Centres(self):
        return self.__training_centres

    @property
    def CompleteSimulationOutput(self):
        return self.__simulation_output

    def __open_new_centre(self):
        # self.__training_centres.append(TrainingCentre())
        return TrainingCentre()

    def __recruit_trainees(self):
        new_trainees = random.randint(20, 30)
        # Append these trainees to waiting list
        self.__trainees["Waiting"] += new_trainees
        return new_trainees  # The number of trainees to generate (not needed but nice)

    def run_simulation(self, gui_enabled=False):
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


            # GUI needs to know status at the end of every month
            full_centres = sum([centre.IsFull for centre in self.__training_centres])
            open_centres = len(self.__training_centres) - full_centres

            self.__simulation_output[month] = {
                "Training": self.__trainees['Training'],
                "Waiting": self.__trainees['Waiting'],
                "Full": full_centres,
                "Open": open_centres
            }

            self.__final_simulation_output = self.__simulation_output[month]

        # End of simulation report
        GUI.print_simulation_results(self.SimulationResults)
        xaxis = []
        yaxis = []
        for key, value in self.__simulation_output.items():
            print(f"Month = {key}")
            print(f"Training = {value['Training']}")

            xaxis.append(key)
            yaxis.append(value['Training'])

        print(xaxis)
        print(yaxis)
        GUI.display_graph(xaxis, yaxis)



    # Testing Getters:
    def get_open_new_centres(self):
        self.__open_new_centre()

    def get_recruit_trainees(self):
        return self.__recruit_trainees()


# Test
sim = Simulation()
sim.run_simulation()
