

"""
 Simple functions, Chapter 2

"""

def square(x):
    """
    :param x:
    :return: square of imput number
    """
    return x**2


#####


def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    for check in [a,b,c,x]:
        if type(check) is str:
            print("Wrong values! ")
            exit(1)
    return a*x**2 + b*x + c




