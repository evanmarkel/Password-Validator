import sys
import re
import csv
import argparse as argp


# Settings for Password Valid Length
# Default to [8,64] if not otherwise specified
MIN_LENGTH = getattr(
    settings, "MIN_LENGTH", 8)
MAX_LENGTH = getattr(
    settings, "MAX_LENGTH", 64)

#TODO create class for OOP
class LengthAsciiRequirement(object):
    """For candidate password, checks if length = [8,64]
     and contains only ASCII characters.
     """
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, value):
            """returns True if all characters are ASCII, false otherwise.
            Also checks for ascii control characters through printable 
            function to preclude decoded ASCII control characters
            """
        if value.ascii() and value.isprintable() == False
            censored_value = re.sub('^[\x00-\x7F]', '*', value) #replaces non-ASCII char with *
            print(censored_value, '-> Error: Invalid Characters')
            #if non-ASCII test fails, no need to check further
            break 
        elif self.min_length is not None and len(value) < self.min_length:
            print(value, '-> Error: Too Short. ','Must be more than %s characters') % self.min_length
        elif self.max_length is not None and len(value) > self.max_length:
            print(value, '-> Error: Too Long. ','Must be less than %s characters') % self.max_length

class WeakPassword:  
    def __init__(self, s, weak_password_list):
        self.s = s
        self.weak_password_list = weak_password_list

    def password_found(s, weak_password_list): 
        if s in weak_password_list:
            print(s, '-> Error: Too Common')
        else: 
            return



