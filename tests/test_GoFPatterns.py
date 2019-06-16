#------------------------------------------------------------------------------
# Python 3.5
# @author Masato Tsuchiya
#------------------------------------------------------------------------------

# 3rd party libraries
import pytest

# GoF Patterns API
from GoF.Singleton import *
from GoF.Factory import *
from GoF.AbstractFactory import *

@pytest.fixture
def common_setup(scope='class', autouse=True):
    def increment(x):
        return x+1
    class A:
        def __init__(self, x):
            self.x = x
        def add(self, B):
            return B.getY() + self.x
    class B:
        def __init__(self, y):
            self.y = y
        def getY(self):
            return self.y
    yield A, B, increment

def test_Singleton(common_setup):
    class DummySingleton2(metaclass=Singleton):
        pass

    s1 = DummySingleton2()
    s2 = DummySingleton2()

    assert s1==s2

def test_Factory(common_setup):
    A, B, increment = common_setup
    f = Factory()
    methodName = "methodName"
    assert methodName not in f.__dict__.keys()
    f.registerConstructor(methodName, increment, x=1)
    assert getattr(f,methodName)()==2
    assert methodName in f.__dict__.keys()

    return

def test_AbstractFactory(common_setup):
    A, B, increment = common_setup
    af = AbstractFactory()
    methodName = "methodName"
    assert methodName not in af.__dict__.keys()
    af.registerConstructor(methodName, A, 2)
    af.registerConstructor(methodName, B, 3)
    assert methodName in af.__dict__.keys()
    a, b = af.createProductFamily(methodName)
    assert a.add(b) == 5

    methodName2 = "methodName2"
    af.registerConstructor(methodName2, increment, 2)
    af.registerConstructor(methodName2, increment, 3)
    x = af.createProductFamily(methodName2)
    assert x == [2+1, 3+1]

    return
