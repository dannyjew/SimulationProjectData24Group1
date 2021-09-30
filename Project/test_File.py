# To run all tests - ensure no instance is created in Simulation class, then in pycharm terminal type pytest -v

import Simulation as S
import Trainees as T
import TrainingCentre as TC
import GUI as G
import matplotlib.pyplot as plt

import unittest.mock as mock
import sys
import os
from unittest.mock import patch

# # # # # # # # # # # # # # # # # # # # # Instances for testing # # # # # # # # # # # # # # # # # # # # #
Testing_Tom = T.Trainees("Training Towers", name="Testing Tom")
Testing_Towers = TC.TrainingCentre("Training Towers")
Sim = S.Simulation(False)


# # # # # # # # # # # # # # # # # # # # # # Trainee Functions # # # # # # # # # # # # # # # # # # # # # #

def test_trainee_name_getter():
    assert Testing_Tom.Name == "Testing Tom"


def test_course_length_getter():
    assert Testing_Tom.Course_length == 3


def test_add_to_training_centre():
    assert Testing_Tom.add_to_training_centre(Testing_Towers)
# Honestly not much to test here, only getters in the class and an add to training centre function that
# wasn't implemented, only returns True so test written around that in case it wants to be used in the future

# # # # # # # # # # # # # # # # # # # # # Training Centre Functions # # # # # # # # # # # # # # # # # # # # #
def test_tc_not_full():
    assert not Testing_Towers.IsFull

def test_add_to_centre():
    added = Testing_Towers.add_trainees(50)
    assert Testing_Towers.Capacity == 50 and added == 50

def test_add_too_many():
    added = Testing_Towers.add_trainees(150)
    assert Testing_Towers.Capacity == 100 and added == 50

def test_is_tc_full():
    Testing_Towers.add_trainees(101)
    assert Testing_Towers.IsFull

# # # # # # # # # # # # # # # # # # # # # # # Simulation Functions # # # # # # # # # # # # # # # # # # # # # # #

# def test_open_centre():                                           # Had originally been tested in older form of
#     old_centre_count = len(Sim.Training_Centres)                  # the code - functionality of increasing training
#     Sim.get_open_new_centres()                                    # centre length moved to outside of sub-function
#     assert old_centre_count + 1 == len(Sim.Training_Centres)      # but code remains the same, test to be kept incase
                                                                    # future refactoring


def test_recruit_trainees_range():
    assert 20 <= Sim.get_recruit_trainees() <= 30


def test_recruit_randomness():                                      # NB This will appear as failed 10% of the time,
    val1 = Sim.get_recruit_trainees()                               # chances of it failing back to back decrease by a
    val2 = Sim.get_recruit_trainees()                               # factor of 10 each time so running tests again
    assert not val1 == val2                                         # should lead to it passing

def test_training_simulation(mocker):
    Test_Sim = S.Simulation(False)
    with mock.patch('builtins.input', side_effect=["6"]):
        Test_Sim.run_simulation()
        required_outputs = {
            "Max Training": 90,
            "Min Training": 60,
            "Waiting": 0,
            "Full": 0,
            "Open": 2
        }
    assert required_outputs["Min Training"] <= Test_Sim.SimulationResults["Training"] <= required_outputs["Max Training"]


def test_waiting_simulation(mocker):
    Test_Sim = S.Simulation(False)
    with mock.patch('builtins.input', side_effect=["6"]):
        Test_Sim.run_simulation()
        required_outputs = {
            "Max Training": 90,
            "Min Training": 60,
            "Waiting": 0,
            "Full": 0,
            "Open": 2
        }
    assert required_outputs["Waiting"] == Test_Sim.SimulationResults["Waiting"]


def test_full_simulation(mocker):
    Test_Sim = S.Simulation(False)
    with mock.patch('builtins.input', side_effect=["6"]):
        Test_Sim.run_simulation()
        required_outputs = {
            "Max Training": 90,
            "Min Training": 60,
            "Waiting": 0,
            "Full": 0,
            "Open": 2
        }
    assert required_outputs["Full"] == Test_Sim.SimulationResults["Full"]

def test_open_simulation(mocker):
    Test_Sim = S.Simulation(False)
    with mock.patch('builtins.input', side_effect=["6"]):
        Test_Sim.run_simulation()
        required_outputs = {
            "Max Training": 90,
            "Min Training": 60,
            "Waiting": 0,
            "Full": 0,
            "Open": 2
        }
    assert required_outputs["Open"] == Test_Sim.SimulationResults["Open"]

# # # # # # # # # # # # # # # # # # # # # # # GUI Test Functions # # # # # # # # # # # # # # # # # # # # # # #

def test_welcome_func_def(mocker):
    length = 3
    opening_centres = 1
    with mock.patch('builtins.input', side_effect=["1"]):           # Mocker passes inputs to function to automate
        assert G.welcome_func() == (length, opening_centres)        # testing
