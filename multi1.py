from curses import KEY_F5
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

def worker3(max3,k3):
    max3.value = 0.1
    k3.value = 0
    while True:
        i = random.random()
        k3.value = k3.value + 1  #probably bottleneck?
        if max3.value < i:
            max3.value = i

def worker4(max4,k4):
    max4.value = 0.1
    k4.value = 0
    while True:
        i = random.random()
        k4.value = k4.value + 1
        if max4.value < i:
            max4.value = i

def worker5(max5,k5):
    max5.value = 0.1
    k5.value = 0
    while True:
        i = random.random()
        k5.value = k5.value + 1  #probably bottleneck?
        if max5.value < i:
            max5.value = i

def worker6(max6,k6):
    max6.value = 0.1
    k6.value = 0
    while True:
        i = random.random()
        k6.value = k6.value + 1
        if max6.value < i:
            max6.value = i

if __name__ == '__main__':
    start = time()
    max1 = Value('f', 0.1); k1 = Value('i', 0)
    max2 = Value('f', 0.1); k2 = Value('i', 0)
    max3 = Value('f', 0.1); k3 = Value('i', 0)
    max4 = Value('f', 0.1); k4 = Value('i', 0)
    max5 = Value('f', 0.1); k5 = Value('i', 0)
    max6 = Value('f', 0.1); k6 = Value('i', 0)

    w1 = Process(target=worker1, args=(max1, k1)); w1.start()
    w2 = Process(target=worker2, args=(max2, k2)); w2.start()
    w3 = Process(target=worker3, args=(max3, k3)); w3.start()
    w4 = Process(target=worker4, args=(max4, k4)); w4.start()
    w5 = Process(target=worker5, args=(max5, k5)); w5.start()
    w6 = Process(target=worker6, args=(max6, k6)); w6.start()
    sleep(9.5)
    w1.terminate()
    w2.terminate()
    w3.terminate()
    w4.terminate()
    w5.terminate()
    w6.terminate()

    print('Max1', max1.value)
    print('Iterations1', k1.value)
    print('Max2', max2.value)
    print('Iterations2', k2.value)
    print('Max', max(max1.value,max2.value))
    print('Iterations', k1.value + k2.value)
    print('Time', time() - start)
