# import Other Classes here
import Simulation as S
import Trainees as T
import Training_Centers as TC

# Testing functions will all go in here:

def Test_Training_Centres(Trainee: Trainee()):
    assert Trainee.get_training_centre is Training_Centre



def Test_Generate_Trainees():
    assert S.generate_trainees() in range(20, 31, 1)

def Test_Max_Capacity(training_centre: Training_Centre()):
    assert training_centre.max() == 100

