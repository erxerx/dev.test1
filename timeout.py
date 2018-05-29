import random
import threading
import time

exitflag = 1


def exiting():
    global exitflag
    exitflag = 0


threading.Timer(9, exiting).start()
i, j, k = 0.1, 0.1, 0
print('Start at', time.ctime(time.time()))
while exitflag:
    i = random.random()
    k = k + 1
    if j < i:
        j = i
print('Exit at', time.ctime(time.time()))
print(i, j, k)
