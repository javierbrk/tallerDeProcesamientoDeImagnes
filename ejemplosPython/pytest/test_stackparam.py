import pytest
@pytest.mark.parametrize("x", [0,1])
@pytest.mark.parametrize("y", [0,1,2,3])

def test_foo(x, y):
    print (x)
    print (y)
    assert x == y
