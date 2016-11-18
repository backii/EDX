

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def evaluate(x):
        return sum(L[len(L)-num-1]*x**num for num in range(len(L)))

    return evaluate



print(general_poly([1, 2, 3, 4])(1))
