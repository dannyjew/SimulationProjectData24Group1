# import Other Classes here
import SImulation_Class as S
import Trainees as T
import Training_Centers as TC

# Testing functions will all go in here:


# def Test_Generate_Trainees():
#     assert S.generate_trainees() in range(20, 31, 1)

# def Test_Add_New_Center(Simulation: S.Simulation):
#     old_centres = Simulation.total_centres
#     Simulation.add_new_centre()
#     assert old_centres + 1 == Simulation.total_centres

# def Test_Training_Centres(Trainee: Trainee()):
#     assert Trainee.get_training_centre is Training_Centre

Testing_Tom = T.Trainees(1, "TestingTowers", name="Testing Tom")

def Test_Trainee_Name_Getter(Testing_Tom):
    assert Testing_Tom.Name() == "Testing Tom"



def Test_Course_Length_Getter(Testing_Tom):
    assert Testing_Tom.Course_length() == 3

def Test_Capacity(training_centre: Training_Centre()):
    assert training_centre.max() == 100

