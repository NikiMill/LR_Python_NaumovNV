from math import *
def f(x):
    number = 0.0
    if (x <= 4):
        if (x == 3.5):
           return  None
        else:
           number = atan(x/5)+(1/(2*x-7))
    elif (4 < x <= 7):
        number = pi**(x/10000)
    else:
        number = abs(floor(3*cos(x)+1))
    return float(number)

def g(x, y):
    return bool((x > -3 and x < 4 and y < -1 and y > -4) or ((x - 3) ** 2 + (y - 4) ** 2 == 9) or (
                (x - 3) ** 2 + (y - 4) ** 2 == 36))

def h(a, b, c):
    count = 1
    if b == 0:
        if (c == 5 or c == -5):
            return "continuum"
        else:
            return str(1)
    else:
        d = 100 * b * b
        if (d > 0):
            if 16 * d != ((a * (2 * b * b) - 8 * b * c)) ** 2:
                count += 1
            count += 1
            return str(count)
print(f(3.5))