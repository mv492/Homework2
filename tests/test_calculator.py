'''My Calculator Test'''
from calculator import add, subtract

def test_addition():
    '''Test that addition function works'''
    assert add(2,2) == 4

def test_subtraction():
    '''Test the subtraction function'''
    assert subtract(4,3) == 1
