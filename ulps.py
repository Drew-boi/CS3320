import sys
import math
import copy

base = sys.float_info.radix
eps = sys.float_info.epsilon
prec = sys.float_info.mant_dig
inf = math.inf
# (spacing) = eps * base ** exponent
def ulps(x : float, y : float) -> int:
    total_steps = 0
    # Check for conditions in which you return infinity
    if x == 0 or y == 0 or x == inf or y == inf or (x < 0 and y > 0) or (y < 0 and x > 0):
        return inf
    if x < 0 and y < 0: # Flip signs to positive if negative
        x = abs(x)
        y = abs(y)

    if x < y:
        #finding exponents/lower bound/upper bound
        exp_x = 0
        lub = 1
        if lub <= x:
            while (lub <= x and x != 1):
                lub *= base
                exp_x += 1
        else:
            while (x < lub and x != 1):
                lub /= base
                exp_x -= 1
            lub *= 2
        gub = 1
        exp_y = 0
        if gub <= y:
            while (gub <= y and y != 1):
                gub *= base
                exp_y += 1
            if gub != 1:
                gub /= 2
        else:
            while (y <= gub and y != 1):
                gub /= base
                exp_y -= 1
            gub *= 2
        # Find step sizes
        x_step = eps * (base ** exp_x)
        y_step = eps * (base ** exp_y)
        if exp_y - exp_x > 1:
            total_steps += math.ceil((lub - x)/ x_step)
            total_steps += math.ceil((y - gub) / y_step)
            while exp_x < exp_y - 1:
                old_lub = copy.copy(lub)
                lub *= base
                exp_x += 1
                step = eps * (base ** exp_x)
                total_steps += math.ceil((lub - old_lub) / step)
        elif exp_x - exp_y == 1:
            total_steps += math.ceil((lub - x)/ x_step)
            total_steps += math.ceil((y - gub) / y_step)
        else:
            total_steps += math.ceil((y - x) / x_step)
        return total_steps

    elif y < x:
        #finding exponents/lower bound/upper bound
        exp_y = 0
        lub = 1
        if lub <= y:
            while (lub <= y and y != 1):
                lub *= base
                exp_y += 1
        else:
            while (y < lub and y != 1):
                lub /= base
                exp_y -= 1
            lub * 2
        gub = 1
        exp_x = 0
        if gub <= x:
            while (gub <= x and x != 1):
                gub *= base
                exp_x += 1
            if gub != 1:
                gub /= 2
        else: 
            while (x <= gub and x != 1):
                gub /= base
                exp_x -= 1
            gub *= 2
        # Find step sizes
        x_step = eps * (base ** exp_x)
        y_step = eps * (base ** exp_y)
        if exp_x - exp_y > 1:
            total_steps += math.ceil((lub - y)/ y_step)
            total_steps += math.ceil((x - gub) / x_step)
            while exp_y < exp_x - 1:
                old_lub = copy.copy(lub)
                lub *= base
                exp_y += 1
                step = eps * (base ** exp_y)
                total_steps += math.ceil((lub - old_lub) / step)
            return total_steps

        elif exp_x - exp_y == 1:
                total_steps += math.ceil((lub - y)/ y_step)
                total_steps += math.ceil((x - gub) / x_step)
                return total_steps
        
        else: 
            total_steps += math.ceil((y - x) / x_step)

    else:
        return total_steps

def main():
    print(ulps(-1.0, -1.0000000000000003)) # 1
    print(ulps(1.0, 1.0000000000000003)) #1
    print(ulps(1.0, 1.0000000000000004)) #2
    print(ulps(1.0, 1.0000000000000005)) #2
    print(ulps(1.0, 1.0000000000000006)) #3
    print(ulps(0.9999999999999999, 1.0)) #1
    print(ulps(0.4999999999999995, 2.0)) #9007199254741001
    print(ulps(0.5000000000000005, 2.0)) #9007199254740987
    print(ulps(0.5, 2.0)) #90071992547409923
    print(ulps(1.0, 2.0)) #4503599627370496
    print(ulps(-1.0, 1.0)) #inf
    print(ulps(-1.0, 0.0)) #inf
    print(ulps(0.0, 1.0)) #inf
    print(ulps(5.0, math.inf)) #inf
    print(ulps(15.0, 100.0)) # 12103423998558208

if __name__ == '__main__':
    main()