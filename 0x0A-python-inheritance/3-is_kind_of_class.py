#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    function to check if the object is an instance of,
    or if the object is an instance of a class
    that inherited from, the specified class
    Attributes:
        obj: attribute to check
        a_class: class to compare to
    Return: true if obj is exactly
    an instance of or if the object is an
    instance of a class that inherited from
    a_class, else false
    """
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
