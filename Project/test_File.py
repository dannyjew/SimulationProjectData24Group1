import sys

import Simulation as S
import Trainees as T
import TrainingCentre as TC



Testing_Tom = T.Trainees("Training Towers", name="Testing Tom")
Testing_Towers = TC.TrainingCentre("Training Towers")
Sim = S.Simulation()
sys.stdin = 1



def test_trainee_name_getter():
    assert Testing_Tom.Name == "Testing Tom"


def test_course_length_getter():
    assert Testing_Tom.Course_length == 3


def test_add_to_training_centre():
    assert Testing_Tom.add_to_training_centre(Testing_Towers)


def test_tc_not_full():
    assert not Testing_Towers.IsFull

def test_is_tc_full():
    Testing_Towers.add_trainees(101)
    assert Testing_Towers.IsFull

def test_open_centre():
    old_centre_count = len(Sim.Training_Centres)
    Sim.get_open_new_centres()
    assert old_centre_count + 1 == len(Sim.Training_Centres)
    sys.stdin = 1

def test_recruit_trainees():
    assert 20 <= Sim.get_recruit_trainees() <= 30

def test_welcome_func_def():
    length = 3
    opening_centres = 1
    assert Sim.get_welcome_func() == (length, opening_centres)
    sys.stdin = 1