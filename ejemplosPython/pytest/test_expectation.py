# content of test_expectation.py
import pytest
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
])
def test_eval(test_input, expected):
    assert  evalFunc (test_input) == expected

def evalFunc (test_input)
    return eval(test_input)
