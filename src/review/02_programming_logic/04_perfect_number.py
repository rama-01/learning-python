for x in range(1, 10000):
    sum = 0
    for y in range(1, x):
        if x % y == 0:
            sum += y
    if x == sum:
        print(x)
