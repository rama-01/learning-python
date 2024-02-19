def biggest_common_divisor(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for n in range(x, 0, -1):
        if x % n == 0 and y % n == 0:
            return n


def smallest_common_multiple(x, y):
    return x * y // biggest_common_divisor(x, y)


print(biggest_common_divisor(9, 12), smallest_common_multiple(9, 12))
