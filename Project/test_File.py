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


def test_add_new_centre():
    old_centers = Simulation_Instance.total_centres
    Simulation_Instance.add_new_centre()
    assert old_centers +1 == Simulation_Instance.total_centres


def test_generate_trainees():
    assert 20 <= Simulation_Instance.generate_trainees() <= 30


def test_add_to_training_centre():
    assert Testing_Tom.add_to_training_centre(Testing_Towers)