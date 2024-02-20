from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


# 主进程将会等待子进程 p1 和 p2 完成其任务，然后才会继续执行主进程后面的代码，join() 方法用于实现主进程对子进程的阻塞等待，直到子进程执行完成。这样可以协调多个进程的执行顺序，确保在需要等待子进程结果时主进程不会提前结束

if __name__ == '__main__':
    main()
