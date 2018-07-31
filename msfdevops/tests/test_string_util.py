"""
Tests for msfdevops string_util module
"""

from msfdevops import * 
import pytest

def test_lowercase_string():
	string = "this is a test string"
	observed = title_string(string)
	expected = "This Is A Test String"

	assert observed == expected, "Lowercase string test failed"

def test_multiple_spaces():
	string = "ThIs String  has MULTIPLE    spAces"
	observed = title_string(string)
	expected = "This String  Has Multiple    Spaces"

	assert observed == expected, "Multiple spaces test failed"