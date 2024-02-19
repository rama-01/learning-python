for x in range(100, 1000):
    low = x % 10
    mid = x // 10 % 10
    high = x // 100
    if low ** 3 + mid ** 3 + high ** 3 == x:
        print(x)