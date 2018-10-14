#------------------------------------------------------------------------------
# Python 3.5
# @author Masato Tsuchiya
#------------------------------------------------------------------------------

# 3rd party libraries
import pytest

# GoF Patterns API
from GoF.Singleton import *
from GoF.Factory import *

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
