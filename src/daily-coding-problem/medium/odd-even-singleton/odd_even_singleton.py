"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances.
And in every even call of getInstance(), return the first instance and in every odd call of getInstance(),
return the second instance.
"""


class DoubleSingleton:
    is_odd = True
    even_instance = None
    odd_instance = None

    def __init__(self, even_value=None, odd_value=None):
        if even_value is not None:
            DoubleSingleton.even_instance = even_value
        if odd_value is not None:
            DoubleSingleton.odd_instance = odd_value

    def add_value(self, value=None):
        """
        Adds a value to the DoubleSingleton class if a slot is available
        """
        if DoubleSingleton.odd_instance is None:
            DoubleSingleton.odd_instance = value
        elif DoubleSingleton.even_instance is None:
            DoubleSingleton.even_instance = value

    def get_instance(self):
        """
        Returns the even instance of DoubleSingleton if the call is even or odd instance if
        the call is odd
        """
        if DoubleSingleton.is_odd:
            DoubleSingleton.is_odd = False
            return DoubleSingleton.odd_instance
        if DoubleSingleton.is_odd is False:
            DoubleSingleton.is_odd = True
            return DoubleSingleton.even_instance
