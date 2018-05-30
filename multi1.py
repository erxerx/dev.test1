import random
from multiprocessing import Process, Value, Array
from time import sleep, time


def worker1(max1,k1):
    max1.value = 0.1
    k1.value = 0
    while True:
        i = random.random()
        k1.value = k1.value + 1  #probably bottleneck?
        if max1.value < i:
            max1.value = i

def worker2(max2,k2):
    max2.value = 0.1
    k2.value = 0
    while True:
        i = random.random()
        k2.value = k2.value + 1
        if max2.value < i:
            max2.value = i

if __name__ == '__main__':
    start = time()
    max1 = Value('f', 0.1)
    k1 = Value('i', 0)
    max2 = Value('f', 0.1)
    k2 = Value('i', 0)

    w1 = Process(target=worker1, args=(max1, k1))
    w1.start()
    w2 = Process(target=worker2, args=(max2, k2))
    w2.start()
    sleep(9.5)
    w1.terminate()
    w2.terminate()

    print('Max1', max1.value)
    print('Iterations1', k1.value)
    print('Max2', max2.value)
    print('Iterations2', k2.value)
    print('Max', max(max1.value,max2.value))
    print('Iterations', k1.value + k2.value)
    print('Time', time() - start)
