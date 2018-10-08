#------------------------------------------------------------------------------
# Python 3.5
# @author Masato Tsuchiya
#------------------------------------------------------------------------------

# def Singleton(cls):
#     """
#     Decorator Singleton
#     """
#     obj = cls()
#     # Always return the same object
#     cls.__new__ = staticmethod(lambda cls: obj)
#
#     # Disable __init__
#     try:
#         del cls.__init__
#     except AttributeError:
#         pass
#     return cls

class Singleton(type):
    """
        Metaclass Singletons only for python3
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                **kwargs)
        return cls._instances[cls]

    @classmethod
    def __instancecheck__(mcs, instance):
        if instance.__class__ is mcs:
            return True
        else:
            return isinstance(instance.__class__, mcs)
