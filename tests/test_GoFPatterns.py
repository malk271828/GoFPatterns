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

def test_Singleton():

    class DummySingleton2(metaclass=Singleton):
        def getX(self):
            return self.x

        def setX(self, x):
            self.x = x

    s1 = DummySingleton2()
    s2 = DummySingleton2()

    assert s1==s2

def test_Factory():
    def increment(x):
        return x+1

    f = Factory()
    methodName = "methodName"
    assert methodName not in f.__dict__.keys()
    f.registerConstructor(methodName, increment, x=1)
    assert getattr(f,methodName)()==2
    assert methodName in f.__dict__.keys()

    return

def test_AbstractFactory():
    class A:
        def __init__(self, x):
            self.x = x
        def add(self, B):
            return B.func() + self.x

    class B:
        def __init__(self, y):
            self.y = y
        def func(self):
            return self.y

    af = AbstractFactory()
    methodName = "methodName"
    assert methodName not in af.__dict__.keys()
    af.registerConstructor(methodName, A, 2)
    af.registerConstructor(methodName, B, 3)
    assert methodName in af.__dict__.keys()
    a, b = [ constructor() for constructor in getattr(af,methodName) ]
    assert a.add(b)==5

    return
