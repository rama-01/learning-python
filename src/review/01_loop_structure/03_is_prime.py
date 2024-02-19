from math import sqrt

num = int(input('please input a integer:'))
end = int(sqrt(num))
is_Prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_Prime = False
        break
if is_Prime and num != 1:
    print('%d is a prime' % num)
else:
    print('%d is not a prime' % num)
