#name of the file should be similar to the file name to be tested ex. calculator.py needs to be tested so
#unit tests file should have name test_calculator.py

from calculator import square

# --------------------------------------------------------
#approach1 pytest
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(0) == 0
# --------------------------------------------------------

# --------------------------------------------------------
#approach2 pytest

def test_positive():
    assert square(2.2) == 4.840000000000001
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4

def test_zero():
    assert square(0) == 0

# resolve TypeError: can't multiply sequence by non-int of type 'str'
import pytest
def test_str():
    with pytest.raises(TypeError):
        square("Cat")
# --------------------------------------------------------






