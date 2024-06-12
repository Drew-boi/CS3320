import math
import sys

def sin(x, n, s = 1): 
    if n == 1:
        return s * x
    else:
        j = n - 1
        s = 1 - s * (x * x / (j * n))
        return sin(x, j - 1, s)

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
    sum = sin(t, 21)
    if (n % 2) == 0:
        return sum
    else:
        return -sum

def main():
    # My Values
    print("Values:")
    print(mySine(1.0e-08) - 1e08) #1e-08
    print(mySine(0.00001)) #9.999999999833334e-06
    print(mySine(0)) #0
    print(mySine(math.pi/2)) #1.0000000000000002
    print(mySine(math.pi)) #-0.0
    print(mySine(100)) #-0.5063656411097555
    print(mySine(-1000)) #-0.8268795405320125
    print(mySine(999999999)) #-0.4101372630100049
    print(mySine(-1000000001)) #nan
    print("ABSOLUTE ERROR:")
    #Absolute Errors
    print(mySine(1.0e-08) - 1.0e-08) #1e-08
    print(mySine(0.00001) - 9.999999999833334e-06) #9.999999999833334e-06
    print(mySine(0) - 0) #0
    print(mySine(math.pi/2) - 1.0000000000000002) #1.0000000000000002
    print(mySine(math.pi) - 0) #-0.0
    print(mySine(100) - -0.5063656411097555) #-0.5063656411097555
    print(mySine(-1000) - -0.8268795405320125) #-0.8268795405320125
    print(mySine(999999999) - -0.4101372630100049) #-0.4101372630100049
    print(mySine(-1000000001)) #nan


if __name__ == '__main__':
    main()
