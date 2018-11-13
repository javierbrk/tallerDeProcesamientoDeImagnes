# content of test_sample.py
# Ref: https://docs.pytest.org/en/latest/
# Agregar atom-python-test desde packages - settings view - install

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
