import pytest
from src.find_substrings.find_substrings import substring

def test_hello():
    string='hello'
    substrings=substring(string)
    assert substrings.list == ['h', 'he', 'hel', 'hell', 'hello', 'e', 'el', 'ell', 'ello', 'l', 'll', 'llo', 'l', 'lo', 'o']
    assert substrings.count == 15

def test_test():
    string='test'
    substrings=substring(string)
    assert substrings.list == ['t', 'te', 'tes', 'test', 'e', 'es', 'est', 's', 'st', 't']
    assert substrings.count == 10

