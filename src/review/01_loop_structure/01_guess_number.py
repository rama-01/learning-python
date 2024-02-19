import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('please insert a number:'))
    if number < answer:
        print('number is too small')
    elif number > answer:
        print('number is too big')
    else:
        print('bingo')
        break
print('you guess %d times' % counter)
if counter >= 7:
    print('you guess too much times')
