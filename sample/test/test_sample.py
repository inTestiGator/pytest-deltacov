"""Tests for sample.py"""

import sample

def test_addition():
    assert sample.addition(9,10) != 21
    assert sample.addition(2,3) == 5

def test_subtraction():
    assert sample.subtraction(2,2) == 0
    assert sample.subtraction(14,6) != 10
