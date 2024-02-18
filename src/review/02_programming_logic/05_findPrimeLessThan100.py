from math import sqrt

for x in range(2, 100):
    is_Prime = True
    for y in range(2, int(sqrt(x)) + 1):
        if x % y == 0:
            is_Prime = False
    if is_Prime:
        print(x)
