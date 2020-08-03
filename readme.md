# Password Validation

## Table of Contents
1. [Problem](#problem)
1. [Approach](#approach)
1. [How to Run](#how-to-run)

## Problem
New [NIST](https://www.nist.gov/)  guidelines provide general rules for protecting the security of user supplied passwords. The goal here is to develop a tool that checks if a password satisfies the following requirements: 
* Has an 8 character minimum
* Has a 64 character maximum
* Allows only ASCII characters (user note: this includes spaces)
* Not be a common password 

## Approach

Performance is key for quick validation of passwords and efficiency of resources. To design for this, the order and data structures checking our four validation parameters must be considered and optimized. The bottleneck in this approach will be matching a candidate password to an entry in a large common password list. This validation will be done last to filter out candidate passwords that fail the other 3 criteria. As speed is a motivation, a candidate password will be removed from further validation if it fails one of the criteria. 

### String Length
I created a class to 

### ASCII Only Characters

### Common Password List Lookup
The codebase is designed to intake any newline delimited list, which can be millions of lines. Thus, it is important to run this function once the other 3 parameters have been met to reduce the number of candidate passwords. The code here was developed with 1M line list linked to in project prompt. To design for unsorted common password input, algorithmic complexity is considered. A sorted list would be on the order of O(n log n) to create and lookups O(log n) which isn't optimal. However, set creation is O(n) and lookup is O(1), providing a much improved runtime. Sets also remove possible duplicates which is fine for our use case and removal would reduce the common password list size and improve runtime. 
\*NOTE: Since lookup is O(1), filtering the common password list for the first 3 parameters as well as the candidate password list would be more costly then leaving as is.\*

## How to Run 
The codebase was developed in Python 3.7 and incompatible with earlier versions due to the ASCII validation implementation used here. Future versions may include compatibility runtime fixes, although with slower overall performance. 
1. Make sure to use Python 3.7 or newer aliased as Python3. 
2. Clone repository to your local folder
3. First time, execute permissions from terminal in home directory of codebase in bash: ```chmod +x run.sh run_tests```
4. To run the main code then enter ```./run.sh```