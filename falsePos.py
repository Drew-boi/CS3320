import math as np
import struct
import sys

def exponent(x : float) -> int:
    # returns the unbiased (true) binary exponent of x as a decimal integer. Remember that
    # subnormals are a special case. Consider 0 to be a subnormal.
    bitX = struct.unpack('Q', struct.pack('d', x))
    exponent = 0
    for i in range (52, 63):
        if bitX[0] & (2 ** i) != 0 :
            exponent += (2 ** (i - 52))
    myBit = 0
    for i in range (0, 52):
        myBit += (2 ** i)
    if exponent > 0 or exponent < 0: 
        return exponent - 1023
    else:
        return exponent - 1022

def ulp(x : float) -> int:
    # returns the magnitude of the spacing between x and its floating-point successor
    myExponent = exponent(x)
    return (2 ** -52) * (2 ** myExponent)

def f(x): 
    return (x ** 4) - 6 * (x ** 3 ) + 12 *(x ** 2) - 10 * x + 3

def ftwo(x):
    return (x ** 3) - 7 * (x ** 2) + 15 * x - 9

def bisect(xl,xu, func ,maxit=1): 
    """ Uses the bisection method to estimate a root of func(x). 
    The method is iterated maxit (default = 20) times. 
    Input: func = name of the function xl = lower guess xu = upper guess 
    Output: xm = root estimate or error message if initial guesses do not bracket solution """ 
    if func(xl)*func(xu)>0:
        return 'initial estimates do not bracket solution' 
    for _ in range(maxit): 
        xm = (xl+xu)/2 
        if func(xm)*func(xl)>0: 
            xl = xm 
        else: 
            xu = xm 
        return xm

def reglafalsi(xl,xu, func,maxint=100000): 
    """ Uses the false position method to estimate a root of func(x). 
    The method is iterated maxit (default = 100000) times. 
    Input: func = name of the function xl = lower guess xu = upper guess 
    Output: xm = root estimate or error message if initial guesses do not bracket solution """ 
    flag = 0
    if func(xl)*func(xu)>0: 
        flag = -1
        return np.nan, flag
    iterations = 0
    UlpClose = 0
    for _ in range(maxint): 
        ourUlp = ulp(xl)
        # Checking if Ulp between is < 1 two iterations in a row
        if xu - xl < ourUlp and UlpClose > 0:
            break
        xm = (func(xu) * xl - func(xl) * xu) / (func(xu) - func(xl)) 
        iterations += 1
        UlpClose = 0
        # Check for Ulp is < 1 first iteration
        if xu - xl < ourUlp:
            UlpClose += 1
        if (func(xm) >= 0 and func(xm) <  sys.float_info.epsilon) or (func(xm) < 0 and func(xm) * -1 < sys.float_info.epsilon): 
            break
        if func(xm)*func(xl)>0: 
            xl = xm 
        else: 
            xu = xm 
    return xm, flag, func(xm), iterations

def main():
    print(reglafalsi(1.5, 2.5, f))
    print(reglafalsi(0, 1.5, f))
    print(reglafalsi(1.5, 2.5, ftwo))
    print(reglafalsi(0, 1.5, ftwo))

if __name__ == '__main__':
    main()