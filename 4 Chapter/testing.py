'''

Unit testing
every function separately
Regression testing
catch reintroduced error were previously fixed
Integration testing
does overall program work ?

Black box testing
Never look into code

Glass Box testing
uses code to guide design


Recall from the lecture that a path-complete glass box test suite would find test cases that go through every possible path
in the code. This is different from black-box testing, because in black-box testing you only have the function specification
For glass-box testing, you actually know how the function you are testing is defined. Thus you can use this definition
to figure out how many different paths through the code exist, and then pick a test suite based on that knowledge.

Undoubtably many - if not all - of the listed tests look like they would be pretty good for testing the function maxOfThree.
However, we want you to think critically about the way maxOfThree is defined - including possible boundary cases -
and pick a set of tests that adequetly and fully tests all paths and boundary conditions. A good first step will be to look at the function
definition and figure out what paths through the code exist. Then, look through the suggested test suites one test
at a time and see if the suite tests every single path.
'''


def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)


print(rem(7,5))






#Exceptions



def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):

    try:
        return item / denom

    except ZeroDivisionError: 
        return 0



print(fancy_divide([0, 2, 4], 0))