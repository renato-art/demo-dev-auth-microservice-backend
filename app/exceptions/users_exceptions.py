"""
    Class created to be an inheritance of the
    other classes created here.
"""
class CustomizedException(Exception):
    
    def __init__(self, message):
        self.message = message
    
    """
        Object method that returns the message
        instantiated in your creation.
    """
    def get_message(self):
        return self.message


"""
    Class created to raise an exception when the
    user provided in the function is empty.
"""
class EmptyUserException(Exception):
    ...
    

"""
    Class created to raise an exception when the
    id provided in the function is not a digit.
"""
class IdIsNotInstanceOfTypeDigitException(CustomizedException):

    def __init__(self, message):
        super.__init__(message)
    

"""
    Class created to raise an exception when the
    user provided in the function doesn't exists.
"""
class NonexistentUserException(CustomizedException):

    def __init__(self, message):
        super.__init__(message)
    