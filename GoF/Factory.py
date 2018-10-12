#------------------------------------------------------------------------------
# Python 3.5
# @author Masato Tsuchiya
#------------------------------------------------------------------------------

#from pyfunctor.functor import *

class Factory:
    def register(self, methodName, constructor, *args, **kargs):
        """register a constructor"""
        # print(list(kargs))
        # f = Functor(list(kargs)) >> constructor
        # setattr(self, methodName, f)
        _args = [constructor]
        _args.extend(args)
        setattr(self, methodName, Functor(*_args, **kargs))

    def unregister(self, methodName):
        """unregister a constructor"""
        delattr(self, methodName)

class Functor:
    def __init__(self, function, *args, **kargs):
        assert callable(function), "function should be a callable obj"
        self._function = function
        self._args = args
        self._kargs = kargs

    def __call__(self, *args, **kargs):
        """call function"""
        _args = list(self._args)
        _args.extend(args)
        _kargs = self._kargs.copy()
        _kargs.update(kargs)
        return self._function(*_args, **_kargs)
