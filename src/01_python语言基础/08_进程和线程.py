# from random import randint
# from time import time, sleep
#
# def download_task(filename):
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
# def main():
#     start = time()
#     download_task('Python从入门到住院.pdf')
#     download_task('Peking Hot.avi')
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
# if __name__ == '__main__':
#     main()

# 代码优化，引入多进程
# from multiprocessing import Process
# from os import getpid
# from random import randint
# from time import time, sleep
#
# def download_task(filename):
#     print('启动下载进程，进程号[%d].' % getpid())
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
# def main():
#     start = time()
#     p1 = Process(target=download_task, args=('Python从入门到住院.pdf',))
#     p1.start()
#     p2 = Process(target=download_task, args=('Peking Hot.avi',))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
# if __name__ == '__main__':
#     main()

# 进程间的通信
# from multiprocessing import Process
# from time import sleep
#
# counter = 0
#
# def sub_task(string):
#     global counter
#     while counter < 10:
#         # flush=True 参数用于控制在调用 print() 函数后是否立即刷新缓冲区并将消息显示在控制台上。当我们将 flush=True 设置为 True 时，print() 函数会立即刷新缓冲区，确保消息立即显示。
#         print(string, end='', flush=True)
#         counter += 1
#         sleep(0.01)
#
# def main():
#     Process(target=sub_task, args=('Ping',)).start()
#     Process(target=sub_task, args=('Pong',)).start()
#
# if __name__ == '__main__':
#     main()

# 改进，引入进程间通信
from multiprocessing import Process, Queue
from time import sleep

counter = 0

def sub_task(string, queue):
    global counter
    while counter < 10:
        queue.put(string)  # 将字符串放入队列
        counter += 1
        sleep(0.01)

def main():
    queue = Queue()  # 创建一个队列对象

    p1 = Process(target=sub_task, args=('Ping', queue))
    p2 = Process(target=sub_task, args=('Pong', queue))

    p1.start()
    p2.start()

    while counter < 10:
        print(queue.get(), end='', flush=True)  # 从队列中获取字符串并打印
        sleep(0.01)

    p1.join()
    p2.join()

if __name__ == '__main__':
    main()

