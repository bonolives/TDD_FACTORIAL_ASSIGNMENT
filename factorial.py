# TDD TEST LAST ASSIGNMENT : Richard Kwizera and Oliver Balyama.

# writing the factorial function

# Defining the function using Iterative approach ( using the 'loop' method)


def factorial_one(var_1):
    """function"""
    answer = 1
    for i in range(1, var_1 + 1):
        answer = answer * i
    return answer


# Defining function using recursion approach.
def factorial_two(var_2):
    """function"""
    if var_2 == 0:
        return 1
    else:
        return var_2 * factorial_two(var_2 - 1)
