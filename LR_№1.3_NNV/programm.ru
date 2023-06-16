import math

print("Введите x: ")
x = int(input(''))

if x > 0 and x != 0:
    y = math.sqrt(x)
    print("x =", '%.0f' % y)
else:
    print("Введите положительное число")
