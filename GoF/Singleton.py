#------------------------------------------------------------------------------
# Python 3.5
# @author Masato Tsuchiya
#------------------------------------------------------------------------------

class Singleton():
    _instance = None
    def __init__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = super().__init__(class_, *args, **kwargs)
        return class_._instance
