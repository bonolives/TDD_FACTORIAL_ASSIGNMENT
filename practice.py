# for range

result = 5
for i in range(result):
    print(i)


result = 6
for i in range(1, result):
    print(i)

"""
There are three methods of calculating factorial in python

1. using a function from the Math Module
2. Iterative approach ( using the for loop)
3. Recursive approach

"""

# using the function from the math module: we use the interactive program of inputing from keyboard

import math

""" function"""
var_1 = int(input("Enter the number: "))
print(math.factorial(var_1))

'''
One option of Defining a test function 
def test_one():
    result = factorial_one(5)
    assert result == 120
'''