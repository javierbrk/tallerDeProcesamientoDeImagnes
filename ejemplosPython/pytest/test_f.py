# content of test_assert1.py
from f import f
def test_function():
    assert f() == 4

def test_assertOdd():
    assert f() % 2 == 0, "value was odd, should be even"
