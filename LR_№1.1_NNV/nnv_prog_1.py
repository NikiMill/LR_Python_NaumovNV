from math import *
def g(x, y):
    return bool((x > -3 and x < 4 and y < -1 and y > -4) or ((x - 3) ** 2 + (y - 4) ** 2 == 9) or (
                (x - 3) ** 2 + (y - 4) ** 2 == 36))

