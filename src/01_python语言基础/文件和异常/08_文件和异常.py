# def main():
#     f = None
#     try:
#         f = open('demo.txt', 'r', encoding='utf-8')
#         print(f.read(), end='')
#     except FileNotFoundError:
#         print('无法打开指定的文件!')
#     except LookupError:
#         print('指定了未知的编码!')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误!')
#     finally:
#         if f:
#             f.close()
#
# if __name__ == '__main__':
#     main()

import time

def main():
    # as f 是用于给打开的文件对象一个别名，以便在代码块中更方便地引用该文件对象。f 是一个自定义的变量名
    # 一次性读取整个文件内容
    with open('demo.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    # 通过for-in循环逐行读取
    with open('demo.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()
    # 读取文件按行读取到列表中
    with open('demo.txt') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    main()