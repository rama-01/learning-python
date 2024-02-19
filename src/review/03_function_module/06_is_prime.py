from math import sqrt


def is_prime(num):
    res = True
    for n in range(2, int(sqrt(num)) + 1):
        if num % n == 0:
            print(n, num // n)
            res = False
            break
    return res


print(is_prime(17))
