import math
import sys

def mySine(x : float) -> float:
    piOne = 3.1416015625
    piTwo = -.000008908910206761537356617
    n = round(x / (piOne + piTwo))
    t = x - (n * piOne)
    t -= (n * piTwo)
    if x ** 2 < sys.float_info.epsilon:
        return x
    if x > 1000000000 or x <  -1000000000:
        return math.nan
    # Use horners rule
    # let y = x^2 and sin(x) = x(1 - y/3! + y^2/5! ...)
    # use odd number of x up to 17th power? For 51 <= p <= 60
    y = t ** 2
    # sum = coefficients[-1]
    # for i in range(len(coefficients) - 1, 0 , -1):
    #     sum = sum * y + coefficients[i - 1]
    
    # sum = 1
    # num = 1
    # den = 21
    # fact = 21
    # for i in range(10, 0, -1):
    #     num = -num * y
    #     fact -= 1
    #     den = den / fact
    #     fact -= 1
    #     den = den / fact
    #     sum += num / den
    # sum = sum * t
    if (n % 2) == 0:
        return sum
    else:
        return -sum

def main():
    print(mySine(1.0e-08) - 1e08) #1e-08
    print(mySine(0.00001)) #9.999999999833334e-06
    print(mySine(0)) #0
    print(mySine(math.pi/2)) #1.0000000000000002
    print(mySine(math.pi)) #-0.0
    print(mySine(100)) #-0.5063656411097555
    print(mySine(-1000)) #-0.8268795405320125
    print(mySine(999999999)) #-0.4101372630100049
    print(mySine(-1000000001)) #nan


if __name__ == '__main__':
    main()