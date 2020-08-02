import sys
import re
import csv

# returns True if all characters are ASCII, false otherwise
# also checks for ascii control characters through printable function to preclude decoded ASCII control characters
def password_is_ascii(s):
    # return len(s) == len(s.encode())
    return s.is_ascii() and s.isprintable()

# returns True if input at least 8 characters
def too_short(s): 
    return len(s) > 7

# returns True if input no more than 64 characters
def too_long(s): 
    return len(s) < 65

