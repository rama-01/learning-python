import sys

f = [x ** 2 for x in range(1, 100)]
print(f)
print(len(f))
print(sys.getsizeof(f))
