import random
import threading
from time import time

keeprunning = 1

def exiting():
    global keeprunning
    keeprunning = 0


start = time()
threading.Timer(9.5, exiting).start()
# our code. at the moment just find max random number
i, j, k = 0.1, 0.1, 0
while keeprunning:
    i = random.random()
    k = k + 1
    if j < i:
        j = i
print('Max', j)
print('Iterations', k)
print('Time', time() - start)
