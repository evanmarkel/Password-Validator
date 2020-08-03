import sys
import re
#import argparse as argp
import time

#Read in password text files. Newline delimited
class ReadInput(object): #TODO have another class readInputSTDIN

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
        return common_list

class Validate(object):
    """For candidate password, checks if length = [8,64],
     contains only ASCII characters,
     and is not found in common password list.
     """
     
    def __init__(self, value, common_password_list, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length
        self.value = value
        self.common_password_list = common_password_list

    def __call__(self, value, common_password_list): 
        """returns True if all characters are ASCII, false otherwise.
        Also checks for ascii control characters through printable 
        function to check for ASCII control characters
        """
        
        if  value.isascii() == False: 
            censored_value = re.sub('[^\x20-\x7E]', '*', value) #replaces non-ASCII char with '*' using regex
            print(censored_value, ' -> Error: Invalid Characters')

        #returns True if input > min_length
        elif self.min_length is not None and len(value) < self.min_length:
            print(value, ' -> Error: Too Short. ')
            
        #returns true if input < max_length    
        elif self.max_length is not None and len(value) > self.max_length:
            print(value, ' -> Error: Too Long. ')

        #checks if in common password list
        elif value in common_password_list:
            print(value, '-> Error: Too Common')

#Read in input files and validate passwords
if __name__ == '__main__':

    # raise error if input criteria not met
    if (len(sys.argv) > 3):
	    raise(Exception('Error: too many input files in /run.sh'))

    elif (len(sys.argv) == 3):
        #input the candidate password newline delimited text file if exists
        input_passwords = sys.argv[1]
        common_passwords = sys.argv[2]

        #benchmark runtime
        start = time.time()

        #read in input files and create password sets
        input = ReadInput().read_candidate_file(input_passwords)
        input_common = ReadInput().read_common_file(common_passwords)

    elif (len(sys.argv) == 2):
        #input_passwords = sys.stdin.readline()
        common_passwords = sys.argv[1]
        input_common = ReadInput().read_common_file(common_passwords)
        while True:
            try:
                value = input() #input('Enter candidate password: \n')
                validator = Validate(value, input_common,8,64)
                validator(value,input_common)
            except EOFError:
                sys.exit()
        
    else:
        raise(Exception('Error: no common password list found'))

    validator = Validate(input,input_common,8,64)
    
    for value in input: 
        validator(value, input_common)