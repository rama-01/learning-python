# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')

# 字符串运算符
# s1 = 'hello' * 3
# print(s1)

# str = 'abc123456'

# str1 = 'hello, world!'
# # 通过内置函数len计算字符串的长度
# print(len(str1))  # 13
# # 获得字符串首字母大写的拷贝
# print(str1.capitalize())  # Hello, world!
# # 获得字符串每个单词首字母大写的拷贝
# print(str1.title())  # Hello, World!
# # 获得字符串变大写后的拷贝
# print(str1.upper())  # HELLO, WORLD!
# # 从字符串中查找子串所在位置
# print(str1.find('or'))  # 8
# print(str1.find('shit'))  # -1
# # 与find类似但找不到子串时会引发异常
# # print(str1.index('or'))
# # print(str1.index('shit'))
# # 检查字符串是否以指定的字符串开头
# print(str1.startswith('He'))  # False
# print(str1.startswith('hel'))  # True
# # 检查字符串是否以指定的字符串结尾
# print(str1.endswith('!'))  # True
# # 将字符串以指定的宽度居中并在两侧填充指定的字符
# print(str1.center(100, '*'))
# # 将字符串以指定的宽度靠右放置左侧填充指定的字符
# print(str1.rjust(50, '#'))
# str2 = 'abc123456'
# # 检查字符串是否由数字构成
# print(str2.isdigit())  # False
# # 检查字符串是否以字母构成
# print(str2.isalpha())  # False
# # 检查字符串是否以数字和字母构成
# print(str2.isalnum())  # True
# str3 = '  jackfrued@126.com '
# print(str3)
# # 获得字符串修剪左右两侧空格之后的拷贝
# print(str3.strip())

# a, b = 5, 10
# print('%d * %d = %d' % (a, b, a * b))

# a, b = 5, 10
# print('{0} * {1} = {2}'.format(a, b, a * b))

# python3.6以后使用语法糖以简化代码
# print(f'{a}*{b}={a * b}')

# list = [1, 2, 3, 4, 5]
# for index in range(len(list)):
#     print(list[index])
# enumerate函数可以同时取出位置索引和对应值
# for index,ele in enumerate(list):
#     print(index,ele)

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
#
# def main():
#     for val in fib(20):
#         print(val)
#
# if __name__ == '__main__':
#     main()

# 练习1 跑马灯文字
# import os
# import time
#
# def main():
#     content = '北京欢迎你为你开天辟地…………'
#     while True:
#         # 清理屏幕上的输出
#         os.system('cls')  # os.system('clear')
#         print(content)
#         # 休眠200毫秒
#         time.sleep(1)
#         content = content[1:] + content[0]
#
# if __name__ == '__main__':
#     main()

# 练习2 生成验证码
import random

# def generate_code(code_len=4):
#     """
#     生成指定长度的验证码
#     :param code_len: 验证码的长度(默认4个字符)
#     :return: 由大小写英文字母和数字构成的随机验证码
#     """
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     return code
#
# code = generate_code()
# print(code)

# 练习3 返回文件的后缀名
# def get_suffix(filename, has_dot=False):
#     """
#     获取文件名的后缀名
#     :param filename: 文件名
#     :param has_dot: 返回的后缀名是否需要带点
#     :return: 文件的后缀名
#     """
#     pos = filename.rfind('.')
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos + 1
#         return filename[index:]
#     else:
#         return ''
#
# print(get_suffix('learning-center.py'))

# 练习4 设计一个函数返回传入列表的最大和第二大的元素
# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2
# # 这里无需考虑x[index] <m1,m2的情况，如果是这样，最后结果是直接返回m1,m2
# print(max2([1,2,12,-12]))

