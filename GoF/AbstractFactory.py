#------------------------------------------------------------------------------
# Python 3.5
# @author Masato Tsuchiya
#------------------------------------------------------------------------------
import abc
from Factory import *

class AbstractFactory(metaclass=abc.ABCMeta):
    def __init__(self):
        factory = Factory()

    @abc.abstractmethod
    def registerConstructor(self, constructor, "args, ""kargs):
        factory.register(constructor, args, kargs)


class PytorchFlow(metaclass=AbstractFactory):
