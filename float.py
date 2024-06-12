import struct
import sys
import math

def sign(x : float) -> int:
    # returns -1 if the x is negative, 0 if x is (either positive or negative) zero, 1 if x is positive.
    if x < 0: return -1
    elif x > 0: return 1
    else: return 0

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


def fraction(x : float) -> float:
    # returns the IEEE fractional part of x as a decimal floating-point number. You must convert
    # binary to decimal. The fraction portion does not include the leading 1 that is not stored.
    bitmaskList = []
    mantissaNum = 0
    bitX = struct.unpack('Q', struct.pack('d', x))
    for i in range(51, -1, -1):
        temp = 2 ** i
        bitmaskList.append(temp)
    for i, bitmask in enumerate(bitmaskList, 1):
        i = -i
        if bitX[0] & bitmask != 0:
            mantissaNum += 2 ** i
    return mantissaNum

def mantissa(x : float) -> float:
    # returns the full IEEE mantissa of x as a decimal floating-point number (which is the same as
    # fraction() + 1 for normalized numbers; same as fraction() for subnormals)
    temp = fraction(x)
    if temp == 0:
        return temp
    else:
        return temp + 1


def is_posinfinity(x : float) -> bool:
    bitmask = 9218868437227405312
    bitmask_two = 18446744073709551615
    bitX = struct.unpack('Q', struct.pack('d', x))
    if bitX[0] & bitmask_two == bitmask:
        return True
    else:
        return False

def is_neginfinity(x : float) -> bool:
    bitmask = 18442240474082181120
    bitmask_two = 18446744073709551615
    bitX = struct.unpack('Q', struct.pack('d', x))
    if bitX[0] & bitmask_two == bitmask:
        return True
    else:
        return False

def ulp(x : float) -> int:
    # returns the magnitude of the spacing between x and its floating-point successor
    myExponent = exponent(x)
    return (2 ** -52) * (2 ** myExponent)

def ulps(x : float, y : float) -> int:
    # returns the number of intervals between x and y by taking advantage of the IEEE standard
    bitX = struct.unpack('Q', struct.pack('d', x))
    bitY = struct.unpack('Q', struct.pack('d', y))
    if x < y:
        return bitY[0] - bitX[0]
    else:
        return bitX[0] - bitY[0]


def main():
    y = 6.5
    subMin = math.nextafter(0,1) # subMin = 5e-324
    print(sign(y)) # 1
    print(sign(0.0)) # 0
    print(sign(-y)) # -1
    print(sign(-0.0)) # 0
    print(exponent(y)) # 2
    print(exponent(16.6)) # 4
    print(fraction(0.0)) # 0.0
    print(mantissa(y)) # 1.625
    print(mantissa(0.0)) # 0.0
    var1 = float('nan')
    print(exponent(var1)) # 1024
    print(exponent(0.0)) # 0
    print(exponent(subMin)) # -1022
    print(is_posinfinity(math.inf)) # True
    print(is_neginfinity(math.inf)) # False
    print(not is_posinfinity(-math.inf)) # True
    print(is_neginfinity(-math.inf)) # True
    print(ulp(y)) # 8.881784197001252e-16
    print(ulp(1.0)) # 2.220446049250313e-16
    print(ulp(0.0)) # 5e-324
    print(ulp(subMin)) # 5e-324
    print(ulp(1.0e15)) # 0.125
    print(ulps(1,2)) # 4503599627370496

if __name__ == '__main__':
    main()