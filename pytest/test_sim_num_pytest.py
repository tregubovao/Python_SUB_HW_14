from os import system
system('cls')
import pytest
from simply_number import simp_num

@pytest.fixture
def sim_num_13():
    return simp_num(13)

@pytest.fixture
def sim_num_100():
    return simp_num(100)

def test_sn_1(sim_num_13):
    assert sim_num_13 == True

def test_sn_2(sim_num_100):
    assert sim_num_100 == False

def test_sn_3(sim_num_100, sim_num_13):
    assert sim_num_100 is not sim_num_13

def test_sn_4(sim_num_100):
    assert isinstance(sim_num_100 , int)

if __name__ == "__main__":
    pytest.main(['-v'])