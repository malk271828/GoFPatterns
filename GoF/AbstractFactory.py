#------------------------------------------------------------------------------
# Python 3.5
# @author Masato Tsuchiya
#------------------------------------------------------------------------------

from pyfunctor.functor import *

class AbstractFactory:
    def __init__(self):
        pass

    def registerConstructor(self, methodName, constructor, *args, **kargs):
        """ register a constructor for lazy evaluation
            If the same method has been already registered,
            additional constructor will be added into a constructor family.
        :param methodName: identifier for virtual constructor
        :param constructor: a function or constructor to create instance.
        :param args: Argument parameters to pass to constructor.
                     Keyword argument cannot be used here.
        :return: N/A
        """
        if hasattr(self, methodName)==True:
            functorList = getattr(self, methodName)
            f = Functor(*args, **kargs) >> constructor
            functorList.append(f)
            setattr(self, methodName, functorList)
        else:
            f = Functor(*args, **kargs) >> constructor
            setattr(self, methodName, [f])

    def unregisterConstructor(self, methodName):
        """
        @fn     public method unregisterConstructor
        @brief  unregister a constructor family
        @param  methodName : identifier for virtual constructor family
        @return N/A
        """
        delattr(self, methodName)

    def createProductFamily(self, methodName):
        return [ constructor() for constructor in getattr(self, methodName) ]