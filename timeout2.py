from threading import Thread
from time import sleep, time

i = 0

def optimize():
    global i
    while True:
        i = i + 1  # dummy op

start = time()
t = Thread(target=optimize, daemon=True)  # run in another thread
t.start()
sleep(9.5)
print('Iterations', i)
print('Time', time() - start)
