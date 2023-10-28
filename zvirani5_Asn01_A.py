'''
CS1026a 2023
Assignment 01 Project 01 - Part A
Zanan Virani
zvirani5
09/27/2023
'''

'''
This program outputs each term of the fibonacci sequence up until a term that the user inputs.
'''

# Opening, as in the assignment
print("Project One (01) - Part A : Fibonacci Sequence")

# Constant variable the user inputs, program will count up to this term (inclusive)
NTH_TERM = int(input("Sequence ends at: "))

# We will be temporarily storing the previous total in this variable.
storage_variable = 0

# We will be using this variable in the addition of the nth number and (n-1)th term.
adding_variable = 1

# This will be the running total that we have.
total = storage_variable + adding_variable

# As said in the assignment tip: The first two terms of the fibonacci sequence are hard-coded in.
# This is why these two lines are included, to match the formatting of the rest of the numbers, but these values are not computed.
print("0: 0 0")
print("1: 1 1")

# for loop, starts from 2 to account for the terms that are hard-coded, NTH_TERM + 1 to make sure we include the last term.
for term in range(2, NTH_TERM + 1):
    print(str(term) + ": ", end='')
    print(total, format(total, ',d'))

# following actions are performed so that the proper total can be printed out in the next iteration of the for loop.
    storage_variable = total
    total += adding_variable
    adding_variable = storage_variable

# Closing, as indicated in assignment.
print("\nEND: Project One (01) - Part A\nZanan Virani zvirani5 251346220")
