# test_spellcheck.py

''' 
Import statements: 
    1. Import pytest and spellcheck modules
'''
### WRITE IMPORT STATEMENTS HERE
import spellcheck
import pytest

# String variables to be tested
alpha = "Checking the length & structure of the sentence."
beta = "This sentence should fail the test"

# Fixture providing the input string (change to alpha or beta to test different cases)


@pytest.fixture
def input_value():
    input = alpha
    return input

# First test function test_length()


def test_length(input_value):
    """
    Tests whether a string has fewer than 10 words and fewer than 50 chars.
    """
    s = input_value  # use fixture inside test
    assert spellcheck.word_count(s) < 10, "Expected fewer than 10 words"
    assert spellcheck.char_count(s) < 50, "Expected fewer than 50 characters"

# Second test function test_struc()


def test_struc(input_value):
    """
    Tests whether a string begins with a capital letter and ends with a period.
    """
    s = input_value.strip()  # local use of fixture value
    first = spellcheck.first_char(s)
    last = spellcheck.last_char(s)

    assert first.isalpha() and first.isupper(
    ), "Expected first character to be an uppercase letter"
    assert last == ".", "Expected sentence to end with a period ('.')"
