"""
Tests for msfdevops math module
"""

from msfdevops import * 
import pytest

@pytest.fixture()
def num_list_3():
	return [1, 2, 3, 4, 5]

def test_mean():
	num_list = [1, 2, 3, 4, 5]
	observed = mean(num_list)
	expected = 3.
	assert observed == expected, "Mean test failed"

def test_mean_list():
	num_tuple = (1, 2, 3, 4, 5)
	with pytest.raises(TypeError):
		mean(num_tuple)

def test_mean_fixture(num_list_3):
	assert mean(num_list_3) == 3