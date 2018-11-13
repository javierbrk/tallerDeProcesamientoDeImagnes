import pytest

def ZeroDivision ():
    1/0

def test_zero_division():
#    with pytest.raises(ZeroDivisionError):
        ZeroDivision()

#verificar que el texto que devuelve la interrupcion tenga informacion esperada
#and if you need to have access to the actual exception info you may use:
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        f(0)
    assert 'maximum recursion' in str(excinfo.value)
    print (excinfo.type)
    print (excinfo.traceback)
    print ("hola")
    assert excinfo.type == 'exa'

def f(a):
    a=a+1
    f(a)
