import sys
import re
#import argparse as argp
import time

#class Settings:
 #   MIN_LENGTH = getattr( "MIN_LENGTH", 8)
  #  MAX_LENGTH = getattr( "MAX_LENGTH", 64)

#Read in password text files. Newline delimiited
class ReadInput(object):

    def read_candidate_file(self, input_passwords):
        password_list = set()
        with open(input_passwords, 'r') as file:
            password_list = file.read().splitlines()
            print(password_list)
        return password_list
    
    def read_common_file(self, common_passwords):
        common_list = set()
        with open(common_passwords, 'r') as file:
            common_list = file.read().splitlines()
            #print(common_list)
        return common_list

class LengthAsciiRequirement(object):
    """For candidate password, checks if length = [8,64]
     and contains only ASCII characters.
     """
     
    def __init__(self, value, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length
        self.value = value

    def __call__(self, value): #changed from value to pw_list
        """returns True if all characters are ASCII, false otherwise.
        Also checks for ascii control characters through printable 
        function to check for ASCII control characters
        """
        print('inlength')
        if  value.isascii() == False: # and value.isprintable():TODO consider whether this is necessary.
            censored_value = re.sub('[^\x00-\x7F]', '*', value) #replaces non-ASCII char with '*' using regex
            print(censored_value, ' -> Error: Invalid Characters')
        #returns True if input > min_length
        elif self.min_length is not None and len(value) < self.min_length:
            print(value, ' -> Error: Too Short. ','Must be more than %s characters') % self.min_length
            
        #returns true if input < max_length    
        elif self.max_length is not None and len(value) > self.max_length:
            print(value, ' -> Error: Too Long. ','Must be less than %s characters') % self.max_length

class WeakPassword():  
    def __init__(self, value, weak_password_list):
        self.value = value
        self.weak_password_list = weak_password_list

    def password_found(self, value, weak_password_list): 
        if value in weak_password_list:
            print(value, '-> Error: Too Common')
        else: 
            return

#Read in input files and validate passwords
if __name__ == '__main__':
    #input the candidate password newline delimited text file. If none, defaults to STDIN
    input_passwords = sys.argv[1]
    common_passwords = sys.argv[2]

    #benchmark runtime
    start = time.time()

    #read in input files and create password sets
    input = ReadInput().read_candidate_file(input_passwords)
    input_common = ReadInput().read_common_file(common_passwords)
  
    #Run validation #TODO need to iterate over lengthascii class 
    for value in input:
        if  value is not None and value.isascii() == False: # and value.isprintable():TODO consider whether this is necessary.
            censored_value = re.sub('[^\x00-\x7F]', '*', value) #replaces non-ASCII char with '*' using regex
            print(censored_value, ' -> Error: Invalid Characters')
        #returns True if input > min_length
        elif value is not None and len(value) < 8:
            print(value, ' -> Error: Too Short. ','Must be more than 8 characters') 
            
        #returns true if input < max_length    
        elif value is not None and len(value) > 64:
            print(value, ' -> Error: Too Long. ','Must be less than 64 characters')

    for value in input: 
       if value in input_common:
           print(value, '-> Error: Too Common')

    #benchmark runtime
    end = time.time()
    print('Time to execute candidate password list validation is: ', end - start,' sec')




       #TODO runtime and optimize. work
       
        #weak = WeakPassword().password_found(value, input_common)