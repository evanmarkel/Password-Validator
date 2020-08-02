#!/bin/bash

##
## Startup script for the Password-Validator source code
## Program written in Python 3.7. Earlier versions incompatible with isascii() function

python3.7 ./src/password_validator.py ./input/input_passwords.txt ./input/common_passwords.txt