#!/usr/bin/python3

import sys
import re
import time

# Read in password text files
class ReadInput(object):

    def read_file(self, pw_file):
        password_list = set()
        with open(pw_file, 'r') as file:
            password_list = file.read().splitlines()
        return password_list


class Validate(object):
    """For candidate password to be valid:
    1) Contains only ASCII characters (exluding control char)
    2) Length within valid range [8,64] default
    3) Is not found in common password list
    """

    def __init__(self, value, common_password_list, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length
        self.value = value
        self.common_password_list = common_password_list

    def __call__(self, value, common_password_list):

        if value.isascii() is False:
            # Replaces non-ASCII char with '*'
            censored_value = re.sub('[^\x00-\x7F]', '*', value)
            print(censored_value, ' -> Error: Invalid Characters')

        elif self.min_length is not None and len(value) < self.min_length:
            print(value, ' -> Error: Too Short.')

        elif self.max_length is not None and len(value) > self.max_length:
            print(value, ' -> Error: Too Long.')

        elif value in common_password_list:
            print(value, '-> Error: Too Common')

if __name__ == '__main__':

    # Benchmark runtime
    # start = time.time()

    # Raise error if input criteria not met
    if (len(sys.argv) > 3):
	    raise(Exception('Error: too many input files in run.sh'))

    elif (len(sys.argv) == 3):
        # Input the candidate password newline delimited text file if exists
        input_passwords = sys.argv[1]
        common_passwords = sys.argv[2]

        # Read in input files and create password sets
        pw_test = ReadInput().read_file(input_passwords)
        pw_common = ReadInput().read_file(common_passwords)
        validator = Validate(pw_test, pw_common, 8, 64)

        for value in pw_test:
            validator(value, pw_common)

    elif (len(sys.argv) == 2):
        # STDIN for manual candidate input
        common_passwords = sys.argv[1]
        pw_common = ReadInput().read_file(common_passwords)
        while True:
            try:
                value = input()
                validator = Validate(value, pw_common, 8, 64)
                validator(value, pw_common)
            except EOFError:
                break

    else:
        raise(Exception('Error: no common password list found'))

    # print('runtime was:' + str(time.time() - start), 'sec')
