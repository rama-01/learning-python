from multiprocessing import Process, Queue
from time import sleep


def sub_task(q, string, other_q):
    counter = 0
    while counter < 5:
        if not q.empty():
            data = q.get()
            print(string, end='', flush=True)
            sleep(0.01)
            other_q.put(data)
            counter += 1


def main():
    q1 = Queue()
    q2 = Queue()
    for _ in range(5):
        q1.put('Ping')
        q2.put('Pong')

    p1 = Process(target=sub_task, args=(q1, 'Ping', q2))
    p2 = Process(target=sub_task, args=(q2, 'Pong', q1))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
