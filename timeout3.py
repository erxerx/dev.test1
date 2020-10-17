import random
from threading import Thread
from time import sleep, time

i = 0
j = 0.1
k = 0.1
l = 0.1

def optimize():
    global i,j,k
    while True:
        k = random.random()
        i = i + 1
        if j < k:
            j = k

start = time()
t = Thread(target=optimize, daemon=True)  # run in another thread
t.start()
while i < 26327807:
    l = random.random()
    if j < l:
        j = l
#sleep(9.5)
print('Iterations', "{:,}".format(i))
print('Max',j)
print('Time', time() - start)
