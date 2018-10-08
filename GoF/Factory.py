#------------------------------------------------------------------------------
# Python 3.5
# @author Masato Tsuchiya
#------------------------------------------------------------------------------

class Factory:
    def register(self, methodName, constructor, *args, **kargs):
        """register a constructor"""
        _args = [constructor]
        _args.extend(args)
        setattr(self, methodName, apply(Functor,_args, kargs))

    def unregister(self, methodName):
        """unregister a constructor"""
        delattr(self, methodName)
