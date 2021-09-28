import SImulation_Class as S
import Trainees as T
import TrainingCentre as TC


Testing_Tom = T.Trainees("Training Towers", name="Testing Tom")
Testing_Towers = TC.TrainingCentre("Training Towers")
Simulation_Instance = S.Simulation("State", ("Initialising", "Running", "Finished"), True)


def test_trainee_name_getter():
    assert Testing_Tom.Name == "Testing Tom"


def test_course_length_getter():
    assert Testing_Tom.Course_length == 3


def test_capacity():
    assert Testing_Towers.Capacity == 100
