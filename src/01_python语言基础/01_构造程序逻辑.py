# 1.水仙花数
# for num in range(100, 1000):
#     a = num // 100
#     b = num // 10 % 10
#     c = num % 10
#     if num == a ** 3 + b ** 3 + c ** 3:
#         print(num)

# 2.反转一个正整数
# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     # 去除前两位数字，以及吧百位数
#     num //= 10
# print(reversed_num)

# 3.百钱百鸡问题
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡:%d,母鸡:%d,小鸡:%d' % (x, y, z))
