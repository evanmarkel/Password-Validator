# Password Validation

## Table of Contents
1. [Problem](#problem)
1. [Approach](#approach)
1. [Implementation](#implementation)
1. [How to Run](#how-to-run)
1. [Testing](#testing)
1. [Further Considerations](#further-considerations)

## Problem
New [NIST](https://www.nist.gov/)  guidelines provide general rules for protecting the security of user supplied passwords. The goal here is to develop a tool that checks if a password satisfies the following requirements: 
* Has an 8 character minimum
* Has a 64 character maximum
* Allows only ASCII characters (user note: this includes spaces)
* Not be a common password 

## Approach

Performance is key for quick validation of passwords and efficiency of resources. To design for this, the order and data structures checking our four validation parameters must be considered and optimized. The bottleneck in this approach will be matching a candidate password to an entry in a large common password list. This validation will be done last to filter out candidate passwords that fail the other 3 criteria. As speed is a motivation, a candidate password will be removed from further validation if it fails one of the criteria. 

## Implementation

The main function calls the file input class to create sets of the two password lists. (Or 1 as candidate password list can be entered through STDIN as explained below). The Validate class evaluates each candidate password through 4 successive conditional statements, printing out the error message to the command line and looping through the next value until the set is evaluated. A more object oriented approach is useful for future changes to criteria or user modification. 

### ASCII Only Characters
Python 3.7 provides a boolean function that tests if all characters in a string are are ASCII. This includes empty strings and ASCII control characters. The latter are allowed as per instructions. The source code replaces all non-ASCII characters with an asterisk with regular expressions and prints the error. 

### String Length
Pretty straightforward. Class attributes can be changed if guidelines change in future. 

### Common Password List Lookup
The codebase is designed to intake any newline delimited list, which can be millions of lines. Thus, it is important to run this function once the other 3 parameters have been met to reduce the number of candidate passwords. The code here was developed with 1M line list linked to in project prompt. To design for unsorted common password input, algorithmic complexity is considered. A sorted list would be on the order of O(n log n) to create and lookups O(log n) which isn't optimal. However, set creation is O(n) and lookup is O(1), providing a much improved runtime when determining if an object is present. Sets remove duplicates which is fine for our use case and removal would reduce the common password list size improving runtime. 
\*NOTE: Since lookup is O(1), filtering the common password list for the first 3 parameters as well as the candidate password list would be more costly then leaving as is.\*

## How to Run 

The codebase was developed in Python 3.7 and incompatible with earlier versions due to the ASCII validation implementation used here. Future versions may include compatibility runtime fixes, although with slower overall performance. 
1. Make sure to use Python 3.7 or newer aliased as Python3 or change run.sh accordingly. 
2. Clone repository to your local folder
3. First time, execute run permissions from terminal in home directory of codebase: ```chmod +x run.sh run_manual_tests.sh run_tests```
4. To run the code then enter ```./run.sh``` in your local environment 
5. Alternately, to manually input candidate passwords from input or ```cat <path to file>``` as per project prompt, enter ```./run_manual_input.sh``` 

## Testing

Several candidate password test sets were utilized and unittesting for edge cases employed to compare code output to expected results. 

## Further Considerations
Argparse is a full featured commandline parser than the simpler sys.argv. The data for this challenge didn't necessitate it, but more robust input handling could be accomplished in future versions. Also, caching the common word list could increase performance for repeated usage of large test files. Further modularity could be implemented for future strong password criteria in separated functions. Also error logging for performance metrics and analytics from dataset performance. 