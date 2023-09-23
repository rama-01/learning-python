"""
输入M和N计算C(M,N)
Version: 0.1
Author: 骆昊
"""


# 1.计算C(m,n)
# m = int(input('m='))
# n = int(input('n='))
# # 计算m!
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fmn = 1
# for num in range(1, m - n + 1):
#     fmn *= num
# print(fm // fn // fmn)


# 2.代码重构
# def factorial(num):
#     res = 1
#     for i in range(1, num + 1):
#         res *= i
#     return res
#
#
# m = int(input('m='))
# n = int(input('n='))
# print(factorial(m) // factorial(n) // factorial(m - n))

# 函数参数
# 3.投掷骰子
# from random import randint
#
#
# def roll_dice(n=2):
#     """摇色子"""
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total
#
#
# print(roll_dice(6))
# print(roll_dice(3))

# 4.可变参数
# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
#
# print(add(1, 2, 3))

# 练习1
'''
def gcd(x, y):
    """求最大公约数"""
    # 三元表达式交换两个变量的值，如果x>y,交换变量的值；否则，不交换
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)

# 调用函数
print(gcd(3, 12))
print(lcm(4,25))
'''

'''print('hello world')'''

