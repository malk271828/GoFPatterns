#------------------------------------------------------------------------------
# Python 3.5
# @author Masato Tsuchiya
#------------------------------------------------------------------------------

from pyfunctor.functor import *

class Factory:
    def registerConstructor(self, methodName, constructor, *args, **kargs):
        """
        @fn     public method registerConstructor
        @brief  register a constructor for lazy evaluation
        @param  methodName : identifier for virtual constructor
        @param  constructor : a function or constructor to create instance.
        @return N/A
        """
        f = Functor(*args, **kargs) >> constructor
        setattr(self, methodName, f)

    def unregisterConstructor(self, methodName):
        """
        @fn     public method unregisterConstructor
        @brief  unregister a constructor
        @param  methodName : identifier for virtual constructor
        @return N/A
        """
        delattr(self, methodName)
