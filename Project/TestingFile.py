# import Other Classes here
import SImulation_Class as S
import Trainees as T
import Training_Centers as TC

# Testing functions will all go in here:

def Test_Training_Centres(Trainee: Trainee()):
    assert Trainee.get_training_centre is Training_Centre



def Test_Generate_Trainees():
    assert S.generate_trainees() in range(20, 31, 1)

def Test_Trainee_Name_Getter(Trainee: T.Trainees(), Trainee_Name: str):
    assert Trainee.Name() = Trainee_Name

def Test_Course_Length_Getter(Trainee: T.Trainees(), Length: int):
    assert Trainee.get_course_length() = Length

def Test_Max_Capacity(training_centre: Training_Centre()):
    assert training_centre.max() == 100

def Test_Add_New_Center(Simulation: S.Simulation):
    old_centres = Simulation.total_centres
    Simulation.add_new_centre()
    assert old_centres + 1 == Simulation.total_centres

