import sys
import re
import csv
import argparse as argp


#TODO create class for OOP
class LengthAsciiRequirement:
    """For candidate password, checks if length = [8,64]
     and contains only ASCII characters.
     """
    def __init__(self):
        pass

    # returns True if all characters are ASCII, false otherwise
    # also checks for ascii control characters through printable function to preclude decoded ASCII control characters
    def password_is_ascii(s):
        # return len(s) == len(s.encode())
        # regex only for earlier versions of python
        # password_is_ascii = lambda s: re.match('^[\x00-\x7F]+$', s) != None
        #TODO use [^\x20-\x7E] instead of above to remove ascii control characters 0-31,127. and replace
        # non-ascii characters with asterixes 
        # s_asterisk = re.sub('^[\x00-\x7F]', '*', s)
        # fix try/except. syntax all off. change approach in morning :-|
        while True: 
            try:
                s.isascii() and s.isprintable() = True
                break
            except: 
                s_asterisk = re.sub('^[\x00-\x7F]', '*', s)
                print(s_asterisk, '-> Error: Invalid Characters')

    # returns True if input at least 8 characters
    def too_short(s): 
        while False: 
            try:
                len(s) < 8 == False
                break
            except: 
                print(s, '-> Error: Too Short')

    # returns True if input no more than 64 characters
    def too_long(s): 
        while False: 
            try:
                len(s) > 64 == False 
                break
            except: 
                print(s, '-> Error: Too Long')

class WeakPassword:  
    def __init__(self, s, weak_password_list):
        self.s = s
        self.weak_password_list = weak_password_list

    def password_found(s, weak_password_list): 
        if s in weak_password_list:
            print(s, '-> Error: Too Common')
        else: 
            return



