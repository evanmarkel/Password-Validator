import sys
import re
import csv
import argparse as argp


#TODO create class for OOP
#Class ValidPasswordSyntax:
 """For candidate password, checks if length = [8,64]
    and contains only ASCII characters.
    """

    # returns True if input at least 8 characters
    def too_short(s): 
        return len(s) < 8

    # returns True if input no more than 64 characters
    def too_long(s): 
        return len(s) > 64

    # returns True if all characters are ASCII, false otherwise
    # also checks for ascii control characters through printable function to preclude decoded ASCII control characters
    def password_is_ascii(s):
        # return len(s) == len(s.encode())
        # regex only for earlier versions of python
        # password_is_ascii = lambda s: re.match('^[\x00-\x7F]+$', s) != None
        return s.is_ascii() and s.isprintable()

#Class WeakPassword:  



