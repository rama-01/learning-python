x = int(input('insert a integer:'))
y = int(input('insert a integer:'))

if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('the most common divisor is %d' % factor)
        print('the most common multiple is %d' % (x * y // factor))
        break
