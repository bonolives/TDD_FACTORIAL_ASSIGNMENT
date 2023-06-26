# Here we import the function from factorial.py file

from factorial import factorial_one, factorial_two

# defining a test function to test the loop method ( factorial_one)

'''
def test_one():
    assert factorial_one(15) == 159
'''


def test_one():
    """ data"""
    assert factorial_one(15) == 1307674368000


# defining a test function to test the recursion approach.
'''
def test_two():
    assert factorial_two(5) == 115
'''


def test_two():
    """ data"""
    assert factorial_two(5) == 120

# END OF ASSIGNMENT

